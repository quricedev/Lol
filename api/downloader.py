from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import html
from user_agent import generate_user_agent

app = Flask(__name__)

PROVIDER_URL = "https://snapdownloader.com/tools/instagram-reels-downloader/download"


@app.route("/api/downloader")
def downloader():
    url = request.args.get("url")

    if not url:
        return jsonify({"status": "error", "message": "url required"}), 400

    try:
        headers = {"User-Agent": generate_user_agent()}
        encoded = requests.utils.quote(url.strip(), safe="")
        target = f"{PROVIDER_URL}?url={encoded}"

        r = requests.get(target, headers=headers, timeout=20)
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
            raise Exception()

        return jsonify({
            "status": "success",
            "data": {
                "download": video,
                "thumbnail": thumb
            }
        })

    except:
        return jsonify({"status": "error", "message": "failed to fetch"}), 500
