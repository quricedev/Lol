import requests
from bs4 import BeautifulSoup
import html
import json
from user_agent import generate_user_agent

PROVIDER_URL = "https://snapdownloader.com/tools/instagram-reels-downloader/download"


def proxy(u):
    return u


def handler(request):
    url = request.query.get("url")

    if not url:
        return (
            400,
            {"Content-Type": "application/json"},
            json.dumps({
                "status": "error",
                "message": "url required"
            }).encode()
        )

    try:
        headers = {
            "User-Agent": generate_user_agent()
        }

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

        return (
            200,
            {"Content-Type": "application/json"},
            json.dumps({
                "status": "success",
                "data": {
                    "download": proxy(video),
                    "thumbnail": thumb
                }
            }).encode()
        )

    except:
        return (
            500,
            {"Content-Type": "application/json"},
            json.dumps({
                "status": "error",
                "message": "failed to fetch"
            }).encode()
  )
