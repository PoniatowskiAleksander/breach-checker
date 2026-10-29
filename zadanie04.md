{"status":"ok"}
172.21.0.1 - - [29/Oct/2026 11:05:18] "GET /health HTTP/1.1" 200 -


7.2
PS C:\studia\sem3\wirtualizzcje\lab\lab4> docker run --rm --network breach-net healthcheck-probe
backend: OK
PS C:\studia\sem3\wirtualizzcje\lab\lab4> docker run --rm healthcheck-probe
backend: UNREACHABLE
PS C:\studia\sem3\wirtualizzcje\lab\lab4> docker run --rm --network breach-net healthcheck-probe
backend: UNREACHABLE

bez flagi --network kontener zostaje podlaczony do sieci domyslnej w ktorej nie dziala dns dockera




7.3

PS C:\studia\sem3\wirtualizzcje\lab\lab4> docker exec backend sh -c "echo notatka > /tmp/notatka.txt"
PS C:\studia\sem3\wirtualizzcje\lab\lab4> docker restart backend
backend
PS C:\studia\sem3\wirtualizzcje\lab\lab4> docker exec backend cat /tmp/notatka.txt
notatka
PS C:\studia\sem3\wirtualizzcje\lab\lab4> docker rm -f backend
backend
PS C:\studia\sem3\wirtualizzcje\lab\lab4> docker run -d --name backend --network breach-net -p 5000:5000 -v ./data/leaked-sha1.txt:/app/data/leaked-sha1.txt:ro breach-checker-backend:v1
1a286bb46ce36dd655f4f27b637bde7805de973a49be8894b6030600130347d6
PS C:\studia\sem3\wirtualizzcje\lab\lab4> docker exec backend cat /tmp/notatka.txt
cat: /tmp/notatka.txt: No such file or directory
PS C:\studia\sem3\wirtualizzcje\lab\lab4> docker run --rm -v breach-dane:/dane alpine sh -c "date >> /dane/historia.txt"

PS C:\studia\sem3\wirtualizzcje\lab\lab4> docker run --rm -v breach-dane:/dane alpine sh -c "date >> /dane/historia.txt; cat /dane/historia.txt"
Thu Oct 29 13:01:34 UTC 2026
Thu Oct 29 13:01:40 UTC 2026
PS C:\studia\sem3\wirtualizzcje\lab\lab4> docker volume ls
DRIVER    VOLUME NAME
local     breach-dane
local     rachunki-wirtualizacje-projekt_pgdata
local     vario-pg-local-data
PS C:\studia\sem3\wirtualizzcje\lab\lab4> docker volume rm breach-dane
breach-dane
PS C:\studia\sem3\wirtualizzcje\lab\lab4>

dlaczego plik w /tmp przetrwał restart, ale nie rm? /tmp przetrwal restart bo restart nie niszczy kontenera, po docker rm juz go nie bylo

dlaczego historia.txt przetrwała, choć oba kontenery zostały usunięte?historia.txt przetrwala bo zostala zapisana w wolumenie ktory jest niezalezny od kontenera

czy lista wycieków przetrwałaby docker rm i dlaczego? tak bo jest podlaczona jako bind mount i nie jest zalezna od kontenera. to fizyczne miejsce na dysku