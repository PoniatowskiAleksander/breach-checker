import os
import re

import psycopg2
import redis
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Cache wyników: klucz = skrót SHA-1, wartość "1"/"0"; po CACHE_TTL sekundach Redis sam usuwa wpis
cache = redis.Redis(host=os.environ["REDIS_HOST"], decode_responses=True,
                    socket_timeout=1, socket_connect_timeout=1)
CACHE_TTL = 300
LOG_URL = os.environ["LOG_URL"]

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

def find_in_db(h):
    conn = connect()
    try:
        with conn.cursor() as cur:
            # %s = parametr zapytania: wartość h nigdy nie staje się częścią kodu SQL
            cur.execute("SELECT EXISTS (SELECT 1 FROM leaked_hashes WHERE hash = %s)", (h,))
            return cur.fetchone()[0]
    finally:
        conn.close()

def find_cached(h):
    # Brak Redisa nie może zatrzymać sprawdzania - wtedy pytamy bazę
    try:
        value = cache.get(h)
        if value is not None:
            return value == "1", "hit"
        found = find_in_db(h)
        cache.set(h, "1" if found else "0", ex=CACHE_TTL)
        return found, "miss"
    except redis.RedisError:
        return find_in_db(h), "niedostępny"

def send_to_log(h, found):
    # Usługa log jest pomocnicza: jej awaria nie może zmienić odpowiedzi dla użytkownika
    try:
        requests.post(LOG_URL, json={"hash_prefix": h[:5], "found": found}, timeout=1)
    except requests.RequestException:
        print("log: usługa niedostępna - odpowiadam bez zapisu próby", flush=True)

@app.post("/check")
def check():
    data = request.get_json(silent=True) or {}
    if "hash" not in data:
        return jsonify({"error": "brak pola 'hash'"}), 400

    h = str(data["hash"]).lower()
    if not re.fullmatch(r"[0-9a-f]{40}", h):
        return jsonify({"error": "pole 'hash' musi być skrótem SHA-1 (40 znaków hex)"}), 400

    found, cache_status = find_cached(h)
    # Pełny SHA-1 popularnego hasła łatwo odwrócić - w logu tylko początek
    print(f"check: hash={h[:5]}... cache={cache_status}", flush=True)
    send_to_log(h, found)
    return jsonify({"found": found})

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    # 0.0.0.0 = nasłuchuj na wszystkich interfejsach kontenera, nie tylko na jego localhost
    app.run(host="0.0.0.0", port=5000)
