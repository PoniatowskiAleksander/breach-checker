import os

from flask import Flask, jsonify, request
from flask_cors import CORS
import re

# Plik z hashami SHA-1 (jeden na linię) - podłączany do kontenera przez bind mount
HASHES_FILE = os.environ.get("HASHES_FILE", "/app/data/leaked-sha1.txt")

app = Flask(__name__)
# Przeglądarka wpuści odpowiedź tylko dla strony z http://localhost:8080 (frontend)
CORS(app, origins=["http://localhost:8080"])


def load_hashes():
    with open(HASHES_FILE, encoding="utf-8") as f:
        return {line.strip().lower() for line in f if line.strip()}


# Wczytanie raz, przy starcie - sprawdzenie w zbiorze (set) trwa O(1)
KNOWN_HASHES = load_hashes()
print(f"Wczytano {len(KNOWN_HASHES)} hashy z {HASHES_FILE}", flush=True)


@app.post("/check")
def check():
    data = request.get_json(silent=True) or {}
    if "hash" not in data:
        return jsonify({"error": "brak pola 'hash'"}), 400

    h = str(data["hash"]).lower()
    if not re.fullmatch(r"[0-9a-f]{40}", h):
        return jsonify({"error": "niepoprawny format hasha"}), 400
    print(f"check: hash={h[:5]}", flush=True)

    # TODO 1: sprawdź, czy h należy do zbioru KNOWN_HASHES (wynik zapisz w zmiennej found)
    found = h in KNOWN_HASHES
    # TODO 2: zwróć JSON {"found": found}
    return jsonify({'found': found})


# @app.get('/health')
# def health():
#     return jsonify({"status": "ok"})
    



if __name__ == "__main__":
    # 0.0.0.0 = nasłuchuj na wszystkich interfejsach kontenera, nie tylko na jego localhost
    app.run(host="0.0.0.0", port=5000)
