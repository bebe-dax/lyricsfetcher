from flask import Blueprint, request, jsonify
from service.lyrics_service import fetch_song_lyrics

lyrics_bp = Blueprint("lyrics", __name__, url_prefix='/api')

@lyrics_bp.route("/lyrics", methods=["GET"])
def get_lyrics():
    title = request.args.get("title")
    artist = request.args.get("artist")

    if not title or not artist:
        return jsonify({"error": "Missing parameters"}), 400
    
    lyrics = fetch_song_lyrics(title, artist)
    if lyrics is None:
        return jsonify({"error": "Song not found"}), 404
    
    return jsonify({"lyrics": lyrics})