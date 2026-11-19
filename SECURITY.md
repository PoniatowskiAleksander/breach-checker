Trivy: Version: 0.76.0 2026-11-19


| Obraz | Rozmiar | HIGH/CRITICAL wszystkie | HIGH/CRITICAL z poprawką |
|---|---|---|---|
| backend:dev | 227 MB | 48 (HIGH 48) | 1 |
| backend:prod | 212 MB | 48 (HIGH 48) | 1 |
| frontend:przed | 229 MB | 28 (HIGH 27, CRITICAL 1) | 28 |
| frontend:prod | 93.7 MB | 0 | 0 |


## Decyzja

Frontend zbudowano w dwóch etapach (multi-stage), więc nie ma w nim Node.js, a po `--pull` ma 0 podatności. Backend ma 48 podatności z obrazu bazowego Debian, z czego 47 nie ma jeszcze poprawki, więc przebudowanie obrazu ich nie usunie. Jedyna z poprawką (zlib1g) zniknie po aktualizacji `python:3.12-slim`. Skan powtarzamy co tydzień i po każdej zmianie Dockerfile.
