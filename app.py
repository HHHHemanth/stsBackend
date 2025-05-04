from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

STATIC_FOLDER = os.path.join(os.getcwd(), "static")
IMAGES_FOLDER = os.path.join(STATIC_FOLDER, "images")
AUDIO_FOLDER = os.path.join(STATIC_FOLDER, "audio")

# Dynamically set the base URL based on the environment
BASE_URL = os.getenv("BASE_URL", "https://stsbackend-1.onrender.com/static")

@app.route('/get-results')
def get_results():
    # Prepare paths for the files
    captured_image_path = os.path.join(IMAGES_FOLDER, "cap.jpg")
    processed_image_path = os.path.join(IMAGES_FOLDER, "res.jpg")
    audio_path = os.path.join(AUDIO_FOLDER, "audres.mp3")
    text_path = os.path.join(STATIC_FOLDER, "kanres.txt")

    # Prepare response data with file URLs
    data = {
        "captured_image": f"{BASE_URL}/images/cap.jpg",
        "processed_image": f"{BASE_URL}/images/res.jpg",
        "kannada_text": f"{BASE_URL}/kanres.txt",
        "audio": f"{BASE_URL}/audio/audres.mp3"
    }

    # Read the Kannada text from file, handle errors if the file doesn't exist
    try:
        if os.path.exists(text_path):
            with open(text_path, "r", encoding="utf-8") as f:
                data["kannada_text"] = f.read()
        else:
            data["kannada_text"] = "Error: Text file not found."
    except Exception as e:
        data["kannada_text"] = f"Error reading text: {e}"

    # Check if images and audio files exist
    if not os.path.exists(captured_image_path):
        data["captured_image"] = "Error: Captured image not found."
    if not os.path.exists(processed_image_path):
        data["processed_image"] = "Error: Processed image not found."
    if not os.path.exists(audio_path):
        data["audio"] = "Error: Audio file not found."

    return jsonify(data)

# This route serves static files like images and audio
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(STATIC_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
