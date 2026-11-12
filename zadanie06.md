PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> docker compose exec backend pytest -v
================================================= test session starts =================================================
platform linux -- Python 3.12.16, pytest-8.4.2, pluggy-1.7.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /app
collected 7 items                                                                                                     

tests/test_check.py::test_leaked_hash_is_found PASSED                                                           [ 14%]
tests/test_check.py::test_unknown_hash_is_not_found PASSED                                                      [ 28%]
tests/test_check.py::test_missing_hash_field PASSED                                                             [ 42%] 
tests/test_check.py::test_plaintext_password_is_rejected PASSED                                                 [ 57%] 
tests/test_check.py::test_uppercase_hash_is_found PASSED                                                        [ 71%]
tests/test_check.py::test_short_hash_is_rejected PASSED                                                         [ 85%] 
tests/test_check.py::test_invalid_hex_is_rejected PASSED                                                        [100%]

================================================== 7 passed in 0.33s ==================================================
PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> docker compose exec backend pytest
================================================= test session starts =================================================
platform linux -- Python 3.12.16, pytest-8.4.2, pluggy-1.7.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /app
collected 7 items                                                                                                     

tests/test_check.py::test_leaked_hash_is_found PASSED                                                           [ 14%]
tests/test_check.py::test_unknown_hash_is_not_found PASSED                                                      [ 28%]
tests/test_check.py::test_missing_hash_field PASSED                                                             [ 42%] 
tests/test_check.py::test_plaintext_password_is_rejected PASSED                                                 [ 57%] 
tests/test_check.py::test_uppercase_hash_is_found FAILED                                                        [ 71%]
tests/test_check.py::test_short_hash_is_rejected PASSED                                                         [ 85%] 
tests/test_check.py::test_invalid_hex_is_rejected PASSED                                                        [100%] 

====================================================== FAILURES =======================================================
____________________________________________ test_uppercase_hash_is_found _____________________________________________

client = <FlaskClient <Flask 'app'>>

    def test_uppercase_hash_is_found(client):
        response = client.post("/check", json={"hash": LEAKED.upper()})
>       assert response.status_code == 200
E       assert 400 == 200
E        +  where 400 = <WrapperTestResponse streamed [400 BAD REQUEST]>.status_code

tests/test_check.py:27: AssertionError
=============================================== short test summary info ===============================================
FAILED tests/test_check.py::test_uppercase_hash_is_found - assert 400 == 200
============================================= 1 failed, 6 passed in 0.50s =============================================
PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> 



testy ioerowaly na zmiennej LEAKED zapisanej malymi literami wiec brak .lower nie powodowal bledu





7.2 



PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> '{"hash":"7c4a8d09ca3762af61e59520943dc26494f8941b"}' | curl.exe -s -o blad.html -w "HTTP %{http_code}\n" -X POST http://localhost:8080/api/check -H "Content-Type: application/json"
 -d '@-'
HTTP 500

> docker compose ps -a
NAME                        IMAGE                     COMMAND                  SERVICE    CREATED       STATUS         
             PORTS
breach-checker-backend-1    breach-checker-backend    "flask --app app run…"   backend    6 days ago    Exited (1) 8 seconds ago
breach-checker-db-1         postgres:16-alpine        "docker-entrypoint.s…"   db         13 days ago   Exited (0) 39 seconds ago
breach-checker-frontend-1   breach-checker-frontend   "/docker-entrypoint.…"   frontend   6 days ago    Up 3 minutes                0.0.0.0:8080->80/tcp, [::]:8080->80/tcp

>  docker inspect --format '{{.State.Status}} {{.State.ExitCode}}' breach-checker-backend-1
exited 1


Plik blad.html zawierał interaktywny panel Werkzeug Debugger ze szczegółowym śladem stosu (traceback), fragmentami kodu źródłowego backendu, ścieżkami systemowymi i nazwami hostów. Na serwerze produkcyjnym stanowi to poważne zagrożenie bezpieczeństwa, ponieważ ujawnia architekturę wewnętrzną aplikacji, ułatwia atakującemu odnalezienie luk, a wbudowany debugger z konsolą mógłby umożliwić wykonanie dowolnego kodu na serwerze

| Cecha | Awaria (crash) | Blokada (czekanie) |
|---|---|---|
| Status w docker compose ps | Exited (1) | Up ... (healthy) |
| CPU w docker stats | - (brak procesu) | ~0% |
| Ostatnie linie logów | Ślad stosu (traceback) z wyjątkiem psycopg2.OperationalError: could not translate host name "db" | Urwane w trakcie żądania: check: hash=... (brak linii POST /check ... 200) |
| Co dostał klient | Strona błędu Werkzeug Debugger (kod HTTP 500) | Błąd 504 Gateway Time-out (od serwera nginx) |
| Po jakim czasie | Natychmiast / po kilku sekundach | Po 60 sekundach (limit czasu oczekiwania nginxa) |








7.3


przed poprawka
PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> curl.exe http://localhost:8080/nginx.conf
server {
    listen 80;

    # Pliki strony (index.html, style.css, script.js)
    location / {
        root /usr/share/nginx/html;
        index index.html;
    }

    # Wszystko pod /api/ nginx przekazuje do usługi backend w sieci Compose
    location /api/ {
        proxy_pass http://backend:5000/;
    }
}




po porawce
PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> curl.exe http://localhost:8080/nginx.conf
<html>
<head><title>404 Not Found</title></head>
<body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx/1.31.6</center>
</body>
</html>





Obraz produkcyjny frontendu nie ma tego problemu, ponieważ w frontend/Dockerfile instrukcja COPY precyzyjnie kopiuje do katalogu serwera WWW wyłącznie pliki strony (index.html, style.css, script.js), a plik nginx.conf trafia do /etc/nginx/conf.d/. Montowanie całego katalogu projektu na serwerze WWW jest ryzykowne, ponieważ ujawnia publicznie pliki konfiguracyjne, Dockerfile oraz inne wrażliwe zasoby projektu bezpośrednio przez HTTP.











