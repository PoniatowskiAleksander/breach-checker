import os
import re

import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

def connect():
    # Dane połączenia przychodzą ze zmiennych środowiskowych ustawionych w docker-compose.yml
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )

# Sprawdzenie bazy raz, przy starcie - bez niej usługa nie ma sensu
conn = connect()
with conn.cursor() as cur:
    cur.execute("SELECT count(*) FROM leaked_hashes")
    print(f"W bazie jest {cur.fetchone()[0]} hashy", flush=True)
conn.close()

@app.post("/check")
def check():
    data = request.get_json(silent=True) or {}
    if "hash" not in data:
        return jsonify({"error": "brak pola 'hash'"}), 400

    h = str(data["hash"]).lower()
    if not re.fullmatch(r"[0-9a-f]{40}", h):
        return jsonify({"error": "pole 'hash' musi być skrótem SHA-1 (40 znaków hex)"}), 400

    # Pełny SHA-1 popularnego hasła łatwo odwrócić - w logu tylko początek
    print(f"check: hash={h[:5]}...", flush=True)

    conn = connect()
    try:
        with conn.cursor() as cur:
            # %s = parametr zapytania: wartość h nigdy nie staje się częścią kodu SQL
            cur.execute("SELECT EXISTS (SELECT 1 FROM leaked_hashes WHERE hash = %s)", (h,))
            found = cur.fetchone()[0]
    finally:
        conn.close()
    return jsonify({"found": found})
    
@app.get("/health")
def health():
    return jsonify({"status": "ok"})
    
if __name__ == "__main__":
    # 0.0.0.0 = nasłuchuj na wszystkich interfejsach kontenera, nie tylko na jego localhost
    app.run(host="0.0.0.0", port=5000)
