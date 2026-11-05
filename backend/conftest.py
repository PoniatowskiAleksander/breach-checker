import pytest

from app import app

@pytest.fixture
def client():
    # Klient testowy Flaska: wysyła żądania do aplikacji bez uruchamiania serwera HTTP
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client



