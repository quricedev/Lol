from flask import Blueprint, request, jsonify
from app.services.scraper import scrape

bp = Blueprint("downloader", __name__)

@bp.route("/api/downloader", methods=["GET"])
def run():
    url = request.args.get("url")

    if not url:
        return jsonify({
            "status": "error",
            "message": "url required"
        }), 400

    data = scrape(url)

    if not data:
        return jsonify({
            "status": "error",
            "message": "failed to fetch"
        }), 500

    return jsonify({
        "status": "success",
        "data": data
    })
