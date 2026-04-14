import requests
from bs4 import BeautifulSoup
import html
from app.utils.headers import headers

PROVIDER = "https://snapdownloader.com/tools/instagram-reels-downloader/download"

def scrape(url):
    try:
        encoded = requests.utils.quote(url.strip(), safe="")
        target = f"{PROVIDER}?url={encoded}"

        r = requests.get(target, headers=headers(), timeout=10)

        if r.status_code != 200:
            return None

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
            return None

        return {
            "download": video,
            "thumbnail": thumb
        }

    except:
        return None
