-- Wykonywany przez obraz postgres tylko przy pierwszym starcie (pusty wolumen)
CREATE TABLE leaked_hashes (
    hash CHAR(40) PRIMARY KEY      -- skrót SHA-1, nigdy hasło jawne
);

-- Tabela pomocnicza: plik może mieć końce linii z Windows (\r) i puste linie
CREATE TEMP TABLE import (line TEXT);
COPY import FROM '/data/leaked-sha1.txt';

INSERT INTO leaked_hashes (hash)
SELECT DISTINCT lower(trim(both E' \r' FROM line))
FROM import
WHERE trim(both E' \r' FROM line) <> '';
