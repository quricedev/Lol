from flask import Blueprint, request, jsonify
from app.services.scraper import fetch_video

bp = Blueprint("downloader", __name__, url_prefix="/api")


@bp.route("/downloader")
def downloader():
    url = request.args.get("url")

    if not url:
        return jsonify({
            "status": "error",
            "message": "url required"
        }), 400

    result = fetch_video(url)

    if not result:
        return jsonify({
            "status": "error",
            "message": "failed to fetch media"
        }), 500

    return jsonify({
        "status": "success",
        "data": result
    })
