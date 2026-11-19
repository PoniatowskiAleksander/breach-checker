# Zadanie 7

## 1. Raport podatności (obrazy :prod po --pull)

```
frontend:prod
│ breach-checker-frontend:prod (alpine 3.24.4) │ alpine │        0        │    -    │

frontend:prod --ignore-unfixed
│ breach-checker-frontend:prod (alpine 3.24.4) │ alpine │        0        │    -    │

backend:prod
Total: 48 (HIGH: 48, CRITICAL: 0)

backend:prod --ignore-unfixed
Total: 1 (HIGH: 1, CRITICAL: 0)
```

Przy 0 podatności Trivy nie wypisuje linii `Total:` (odpowiada to Total: 0).

--pull wyzerował podatności frontendu: nowy nginx:alpine (Alpine 3.24.4) zawiera poprawki wszystkich 28 podatności. W backendzie wynik się nie zmienił, bo python:3.12-slim nie został zaktualizowany (wszystkie kroki CACHED), a 47 z 48 podatności Debiana i tak nie ma jeszcze poprawki.

## 2. Utwardzenie kontenera

Błąd przed dodaniem tmpfs
```
backend-1  | FileNotFoundError: [Errno 2] No usable temporary directory found in ['/tmp', '/var/tmp', '/usr/tmp', '/app']
```

Po dodaniu tmpfs:
```
PS> docker compose exec backend touch /etc/test
touch: cannot touch '/etc/test': Read-only file system
PS> docker compose exec backend touch /tmp/test
PS> docker compose exec backend grep CapEff /proc/1/status
CapEff: 0000000000000000
```

Konfiguracja dev:
```
PS> docker compose exec backend pytest
platform linux -- Python 3.12.16, pytest-8.4.2, pluggy-1.7.0
rootdir: /app
collected 7 items

tests/test_check.py .......                                              [100%]

=========================== 7 passed in 0.36s ===========================
```

`read_only` blokuje zapis w całym systemie plików kontenera, więc nawet root nie podmieni plików ani nie doinstaluje narzędzi. `cap_drop: ALL` odbiera procesowi wszystkie uprawnienia jądra (capabilities), a `no-new-privileges` nie pozwala zyskać nowych uprawnień, np. przez programy z setuid. `USER appuser` tylko zmienia użytkownika na zwykłego, który nie może pisać do plików roota, a `read_only` blokuje zapis dla wszystkich, także dla roota.

## 3. Sekret w usuniętym pliku

```
PS> docker run --rm sekret-demo:plik ls /tmp
PS> docker history sekret-demo:plik
IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
15087ab8d3c3   41 seconds ago   RUN /bin/sh -c rm /tmp/klucz.txt # buildkit     8.19kB    buildkit.dockerfile.v0
<missing>      42 seconds ago   RUN /bin/sh -c test -s /tmp/klucz.txt && ech…   4.1kB     buildkit.dockerfile.v0
<missing>      43 seconds ago   COPY klucz.txt /tmp/klucz.txt # buildkit        12.3kB    buildkit.dockerfile.v0
<missing>      13 days ago      CMD ["/bin/sh"]                                 0B        buildkit.dockerfile.v0
<missing>      13 days ago      ADD alpine-minirootfs-3.22.8-x86_64.tar.gz /…   8.97MB    buildkit.dockerfile.v0
```

Odzyskana zawartość pliku z warstw obrazu:
```
tajny-klucz-aleksander
```

`RUN rm` tworzy nową warstwę, która tylko oznacza plik jako usunięty, a warstwa z `COPY klucz.txt` nadal istnieje w obrazie i można z niej odczytać plik. Klucz należało przekazać przez `docker build --secret` i `RUN --mount=type=secret`, wtedy nie trafia do żadnej warstwy.

