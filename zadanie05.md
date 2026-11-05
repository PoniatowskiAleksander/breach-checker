1.
=> [backend] resolving provenance for metadata file                                                                                0.0s 
[+] Running 7/7
 ✔ breach-checker-backend               Built                                                                                       0.0s 
 ✔ breach-checker-frontend              Built                                                                                       0.0s 
 ✔ Container breach-checker-backend-3   Removed                                                                                     0.2s 
 ✔ Container breach-checker-backend-2   Removed                                                                                     0.2s 
 ✔ Container breach-checker-backend-1   Healthy                                                                                    38.2s 
 ✔ Container breach-checker-frontend-1  Started                                                                                    38.1s 
 ✔ Container breach-checker-db-1        Healthy                                                                                     6.1s 
PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> ^C
PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> docker compose ps
NAME                        IMAGE                     COMMAND                  SERVICE    CREATED         STATUS                   PORTS
breach-checker-backend-1    breach-checker-backend    "python app.py"          backend    3 minutes ago   Up 3 minutes (healthy)   5000/tcp
breach-checker-db-1         postgres:16-alpine        "docker-entrypoint.s…"   db         3 minutes ago   Up 3 minutes (healthy)   5432/tcp
breach-checker-frontend-1   breach-checker-frontend   "/docker-entrypoint.…"   frontend   3 minutes ago   Up 2 minutes             0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> 





2.
PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> '{"hash":"bc45408273d7e1914b741c3407b0b559764f7876"}' | curl.exe -X POST http://localhost:8080/api/check
 -H "Content-Type: application/json" -d '@-'
>>
{"found":true}



pod compose down i up
PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> '{"hash":"bc45408273d7e1914b741c3407b0b559764f7876"}' | curl.exe -X POST http://localhost:8080/api/check
 -H "Content-Type: application/json" -d '@-'
>>
{"found":true}


po down -v
PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> '{"hash":"bc45408273d7e1914b741c3407b0b559764f7876"}' | curl.exe -X POST http://localhost:8080/api/check
 -H "Content-Type: application/json" -d '@-'
>>
{"found":false}




Skrót przetrwał down bo nie zostala uzyta flaga -v ktora usuwa wolumen. po uzyciu flagi -v wolumen zostal usuniety jednak po uruchomieniu zostal wykonant init.sql ktory dopisal odpowiednie rekordy do bazy



3.

PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> docker compose ps
NAME                        IMAGE                     COMMAND                  SERVICE    CREATED          STATUS                    PORTS
breach-checker-backend-1    breach-checker-backend    "python app.py"          backend    10 minutes ago   Up 10 minutes (healthy)   5000/tcp
breach-checker-backend-2    breach-checker-backend    "python app.py"          backend    2 minutes ago    Up 2 minutes (healthy)    5000/tcp
breach-checker-backend-3    breach-checker-backend    "python app.py"          backend    2 minutes ago    Up 2 minutes (healthy)    5000/tcp
breach-checker-db-1         postgres:16-alpine        "docker-entrypoint.s…"   db         6 days ago       Up 10 minutes (healthy)   5432/tcp
breach-checker-frontend-1   breach-checker-frontend   "/docker-entrypoint.…"   frontend   10 minutes ago   Up About a minute         0.0.0.0:8080->80/tcp, [::]:8080->80/tcp





PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> docker compose exec frontend nslookup backend
Server:         127.0.0.11
Address:        127.0.0.11:53

Non-authoritative answer:

Non-authoritative answer:
Name:   backend
Address: 172.22.0.6
Name:   backend
Address: 172.22.0.3
Name:   backend
Address: 172.22.0.5




przed:
backend-1  | check: hash=bc454...
backend-1  | 172.22.0.4 - - [05/Nov/2026 12:16:00] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.22.0.4 - - [05/Nov/2026 12:16:00] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.22.0.4 - - [05/Nov/2026 12:16:00] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.22.0.4 - - [05/Nov/2026 12:16:00] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.22.0.4 - - [05/Nov/2026 12:16:00] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.22.0.4 - - [05/Nov/2026 12:16:00] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...


po:
backend-3  | 127.0.0.1 - - [05/Nov/2026 12:11:09] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [05/Nov/2026 12:11:39] "GET /health HTTP/1.1" 200 -
backend-3  | check: hash=bc454...
backend-3  | 172.22.0.4 - - [05/Nov/2026 12:11:45] "POST /check HTTP/1.1" 200 -
backend-3  | check: hash=bc454...
backend-3  | 172.22.0.4 - - [05/Nov/2026 12:11:45] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.22.0.4 - - [05/Nov/2026 12:11:45] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.22.0.4 - - [05/Nov/2026 12:11:45] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...



2-3 zdania: dlaczego przed restartem frontendu ruch trafiał do jednej repliki (wskazówka: kiedy nginx tłumaczy nazwę backend na adresy - patrz krok 2); dlaczego skalowanie byłoby niemożliwe, gdyby backend nadal miał ports: "5000:5000".:

Dns w frontend jest rozpoznawany raz przy starcie i zapamietywany. dopiero po restarcie frontend dowiaduje sie ze jest wiecej backendow i rozdziela na nie zapytania.
Skalowanie byłoby niemożliwe, gdyby backend nadal miał ports: "5000:5000", ponieważ tylko jeden kontener może zająć dany port na hoście - przy kolejnych replikach Docker zgłosiłby konflikt portów