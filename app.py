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


@app.route("/ishihara")
@app.route("/ishihara.html")
def ishihara_page():
    return send_from_directory(BASE_DIR, "ishihara.html")


@app.route("/report.txt")
def serve_report():
    return send_from_directory(BASE_DIR, "report.txt", mimetype="text/plain; charset=utf-8")


@app.route("/audit.txt")
def serve_audit():
    return send_from_directory(BASE_DIR, "audit.txt", mimetype="text/plain; charset=utf-8")


@app.route("/api/results")
@app.route("/results.json")
@app.route("/result.json")
def get_results():
    target = RESULTS_PATH
    if not target.exists():
        alt_target = BASE_DIR / "result.json"
        if alt_target.exists():
            target = alt_target
        else:
            return jsonify({"error": True, "message": "results.json not found"}), 404
    with open(target, "r", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)


@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/samples/<path:filename>")
def serve_sample(filename):
    samples_dir = BASE_DIR / "samples"
    return send_from_directory(samples_dir, filename)


@app.route("/data/<path:filename>")
def serve_data(filename):
    data_dir = BASE_DIR / "data"
    target = data_dir / filename
    if target.exists():
        return send_from_directory(data_dir, filename)
    preset_dir = BASE_DIR / "samples" / "presets"
    preset_target = preset_dir / filename
    if preset_target.exists():
        return send_from_directory(preset_dir, filename)
    return jsonify({"error": True, "message": f"File {filename} not found"}), 404


@app.route("/logo.png")
def serve_logo():
    return send_from_directory(BASE_DIR, "logo.png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

