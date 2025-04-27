import lyricsgenius
import os
from dotenv import load_dotenv

load_dotenv()

genius = lyricsgenius.Genius(os.getenv("GENIUS_API_TOKEN"))

def fetch_song_lyrics(title: str, artist: str) -> str | None:
    song = genius.search_song(title, artist)
    if song is None:
        return None
    return song.lyrics