from bark import SAMPLE_RATE, generate_audio, preload_models
from flask import Flask, request, jsonify

preload_models()

app = Flask(__name__)

@app.route("/bark", methods=["POST"])
def generate_tts():
    text = request.json.get("text")
    if not text:
        return jsonify({"error": "Missing text input"}), 400
    audio_data = generate_audio(text)
    return jsonify({"audio": audio_data}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)