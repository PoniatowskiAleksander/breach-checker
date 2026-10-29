1.

[+] Running 6/6
 ✔ breach-checker-backend               Built                                                                                                               0.0s 
 ✔ breach-checker-frontend              Built                                                                                                               0.0s 
 ✔ Network breach-checker_default       Created                                                                                                             0.1s 
 ✔ Container breach-checker-db-1        Healthy                                                                                                             6.9s 
 ✔ Container breach-checker-backend-1   Started                                                                                                             7.1s 
 ✔ Container breach-checker-frontend-1  Started                                                                                                             7.4s 
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




Przetrwal down bo bez flagi -v nie jest usuwany wolumen. 89 hashy ktore sa w bazie wynika z tego ze sa one w obrazie.