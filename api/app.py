from flask import Flask
from controller.lyrics_controller import lyrics_bp

app = Flask(__name__)
app.register_blueprint(lyrics_bp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)