"""
Simple Flask API for the CVD Restormer dashboard.

Serves the contents of results.json at /api/results.
To use your real notebook output instead of the sample numbers,
just overwrite results.json with the same shape (see README.md).

Run:
    pip install flask flask-cors
    python app.py
Then open index.html in your browser (it fetches from
http://localhost:5000/api/results).
"""

import json
from pathlib import Path

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # also allows index.html to be opened as a local file:// page and still fetch this API

BASE_DIR = Path(__file__).parent
RESULTS_PATH = BASE_DIR / "results.json"


@app.route("/")
def dashboard():
    # Serves index.html directly, so http://localhost:5000/ shows the dashboard
    # instead of a 404 — no need to open index.html separately.
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/api/results")
def get_results():
    if not RESULTS_PATH.exists():
        return jsonify({"error": True, "message": "results.json not found"}), 404
    with open(RESULTS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)


@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/samples/<path:filename>")
def serve_sample(filename):
    samples_dir = BASE_DIR / "samples"
    return send_from_directory(samples_dir, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
