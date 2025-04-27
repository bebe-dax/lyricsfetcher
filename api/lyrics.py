# lyricsgeniusの動作確認用のAPI
# Pythonファイルを直接実行すればエラーにならないが、ブラウザやターミナルからリクエストを送ると403エラーになる

from flask import Flask, request, jsonify
import lyricsgenius
from dotenv import load_dotenv
import os

# load_dotenv()
# genius = lyricsgenius.Genius(os.getenv("GENIUS_API_TOKEN"))

# app = Flask(__name__)

# @app.route("/api/lyricsdummy", methods=["GET"])
# def get_lyrics():
#     title = request.args.get("title")
#     artist = request.args.get("artist")
#     if not title or not artist:
#         return jsonify({"error": "Missing parameters"}), 400
    
#     song = genius.search_song(title, artist)

#     if song is None:
#         return jsonify({"error": "Song not found"}), 404
#     return jsonify({"lyrics": song.lyrics})

# if __name__ == "__main__":
#     app.run(port=5000)


# Pythonファイルを直接自校した場合は、正常にAPIを実行できる
# #トークン設定
# load_dotenv()
# token = os.getenv("GENIUS_API_TOKEN")
# genius = lyricsgenius.Genius(token)

# #検索したいアーティスト、楽曲名を設定
# artist_name = '米津玄師'
# track = 'Lemon'

# #アーティストを検索
# artist = genius.search_artist(artist_name, max_songs=5)

# #指定した曲を検索して、該当する曲の歌詞を取得
# song_lyrics = genius.search_song(track, artist.name).lyrics

# print(song_lyrics)

load_dotenv()

genius = lyricsgenius.Genius(os.getenv("GENIUS_API_TOKEN"))

title = 'Star'
artist = '星野源'

def fetch_song_lyrics(title: str, artist: str) -> str | None:
    song = genius.search_song(title, artist)
    if song is None:
        return None
    print(song.lyrics)
    return song.lyrics

fetch_song_lyrics(title, artist)