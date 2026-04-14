from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import html

app = Flask(__name__)

PROVIDER_URL = "https://snapdownloader.com/tools/instagram-reels-downloader/download"

@app.route("/api/downloader")
def downloader():
    url = request.args.get("url")

    if not url:
        return jsonify({"status": "error", "message": "url required"}), 400

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
            "Accept": "*/*"
        }

        encoded = requests.utils.quote(url.strip(), safe="")
        target = f"{PROVIDER_URL}?url={encoded}"

        r = requests.get(target, headers=headers, timeout=10)

        if r.status_code != 200:
            return jsonify({
                "status": "error",
                "message": f"provider failed {r.status_code}"
            }), 500

        soup = BeautifulSoup(r.text, "html.parser")

        video = None
        thumb = None

        for a in soup.find_all("a", href=True):
            link = html.unescape(a["href"]).strip()

            if "cdninstagram.com" in link and ".mp4" in link:
                video = link

            if "cdninstagram.com" in link and any(x in link for x in [".jpg", ".jpeg", ".png"]):
                thumb = link

        if not video:
            return jsonify({
                "status": "error",
                "message": "no media found (blocked or invalid)"
            }), 404

        return jsonify({
            "status": "success",
            "data": {
                "download": video,
                "thumbnail": thumb
            }
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


app = app
