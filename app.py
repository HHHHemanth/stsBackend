from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/get-results')
def get_results():
    # Assuming these files are in the 'static' folder in the same directory
    base_url = "http://192.168.113.145:5000/static"

    data = {
        "captured_image": f"{base_url}/images/cap.jpg",
        "processed_image": f"{base_url}/images/res.jpg",
        "kannada_text": f"{base_url}/kanres.txt",
        "audio": f"{base_url}/audio/audres.mp3"  # Change this to the dynamic name if required
    }

    try:
        with open("static/kanres.txt", "r", encoding="utf-8") as f:
            data["kannada_text"] = f.read()
    except Exception as e:
        data["kannada_text"] = f"Error reading text: {e}"

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
