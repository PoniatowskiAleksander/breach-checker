from datetime import datetime, timezone

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.post("/log")
def log_attempt():
    data = request.get_json(silent=True) or {}
    # Tylko metadane próby - usługa log nie dostaje pełnego skrótu, hasła ani dostępu do bazy
    entry = {
        "time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "hash_prefix": str(data.get("hash_prefix", ""))[:5],
        "found": bool(data.get("found")),
    }
    print(f"log: {entry}", flush=True)
    return jsonify({"status": "logged"}), 201

@app.get("/health")
def health():
    return jsonify({"status": "ok"})
