# Zadanie 8

## 1. Frontend w pipeline

Nieudane uruchomienie (build-frontend):
https://github.com/PoniatowskiAleksander/breach-checker/actions/runs/45827530729

```
> [lint 5/5] RUN htmlhint index.html:
0.253 
0.271    /site/index.html
0.272       L16 |        <>Breach Checker
0.272                    ^ Special characters must be escaped : [ < ]. (spec-char-escape)
0.272       L16 |        <>Breach Checker
0.272                     ^ Special characters must be escaped : [ > ]. (spec-char-escape)
0.272 
0.275 Scanned 1 files, found 2 errors in 1 files (25 ms)
```

Następne, zielone uruchomienie:
https://github.com/PoniatowskiAleksander/breach-checker/actions/runs/45827592970

W zielonym uruchomieniu verify pobiera z rejestru oba obrazy z tagiem tego samego commita, czyli te, które trafią na produkcję. Wcześniej z rejestru pochodził tylko backend, a frontend był budowany od nowa na runnerze.

## 2. latest po weryfikacji

Nieudany verify, pominięty promote:
https://github.com/PoniatowskiAleksander/breach-checker/actions/runs/45819046257

Następne, zielone uruchomienie:
https://github.com/PoniatowskiAleksander/breach-checker/actions/runs/45819489375

Po nieudanym uruchomieniu latest backendu nadal wskazywał obraz z commita 4465414, ostatni, który przeszedł weryfikację. Ktoś, kto pobiera obraz bez podawania tagu, dostaje latest, więc nie otrzyma zepsutej wersji.

## 3. Publiczny pakiet

```
PS C:\studia\sem3\wirtualizzcje\lab\lab08\breach-checker> docker logout ghcr.io
>>
Removing login credentials for ghcr.io
PS C:\studia\sem3\wirtualizzcje\lab\lab08\breach-checker> docker pull "${img}:latest"
>>
latest: Pulling from poniatowskialeksander/breach-checker-backend
Digest: sha256:523caf1efce10b03a6cdc98315ae86f22535f94b8018ad3fa0a2c129ea6bc258
Status: Image is up to date for ghcr.io/poniatowskialeksander/breach-checker-backend:latest
ghcr.io/poniatowskialeksander/breach-checker-backend:latest
PS C:\studia\sem3\wirtualizzcje\lab\lab08\breach-checker> docker pull "${img}:$sha"
8d733a8bff18f5f8929489959b2beea8a30e5fe5: Pulling from poniatowskialeksander/breach-checker-backend
Digest: sha256:523caf1efce10b03a6cdc98315ae86f22535f94b8018ad3fa0a2c129ea6bc258
Status: Image is up to date for ghcr.io/poniatowskialeksander/breach-checker-backend:8d733a8bff18f5f8929489959b2beea8a30e5fe5
ghcr.io/poniatowskialeksander/breach-checker-backend:8d733a8bff18f5f8929489959b2beea8a30e5fe5
PS C:\studia\sem3\wirtualizzcje\lab\lab08\breach-checker> docker images --digests $img
>>
REPOSITORY                                             TAG                                        DIGEST                                                                    IMAGE ID       CREATED          SIZE
ghcr.io/poniatowskialeksander/breach-checker-backend   8d733a8bff18f5f8929489959b2beea8a30e5fe5   sha256:523caf1efce10b03a6cdc98315ae86f22535f94b8018ad3fa0a2c129ea6bc258   523caf1efce1   32 minutes ago   212MB
ghcr.io/poniatowskialeksander/breach-checker-backend   bez-tokenu                                 sha256:523caf1efce10b03a6cdc98315ae86f22535f94b8018ad3fa0a2c129ea6bc258   523caf1efce1   32 minutes ago   212MB
ghcr.io/poniatowskialeksander/breach-checker-backend   latest                                     sha256:523caf1efce10b03a6cdc98315ae86f22535f94b8018ad3fa0a2c129ea6bc258   523caf1efce1   32 minutes ago   212MB
PS C:\studia\sem3\wirtualizzcje\lab\lab08\breach-checker> docker push "${img}:latest"
>>
The push refers to repository [ghcr.io/poniatowskialeksander/breach-checker-backend]
83a14706aa6d: Waiting
83a14706aa6d: Layer already exists
75e821680269: Layer already exists
183f2e7a77cf: Layer already exists
c5c488c36774: Layer already exists
407ae2fe0db4: Layer already exists
e3e428093f5e: Layer already exists
286d8c291daa: Layer already exists
42f199b00a0a: Layer already exists
latest: digest: sha256:523caf1efce10b03a6cdc98315ae86f22535f94b8018ad3fa0a2c129ea6bc258 size: 2199
PS C:\studia\sem3\wirtualizzcje\lab\lab08\breach-checker> docker tag "${img}:latest" "${img}:bez-tokenu"
>>
PS C:\studia\sem3\wirtualizzcje\lab\lab08\breach-checker> docker push "${img}:bez-tokenu"
>>
The push refers to repository [ghcr.io/poniatowskialeksander/breach-checker-backend]
c5c488c36774: Waiting
c5c488c36774: Layer already exists
286d8c291daa: Layer already exists
75e821680269: Layer already exists
183f2e7a77cf: Layer already exists
30cf67d7101c: Layer already exists
83a14706aa6d: Layer already exists
407ae2fe0db4: Layer already exists
42f199b00a0a: Layer already exists
error from registry: unauthenticated: User cannot be authenticated with the token provided.
PS C:\studia\sem3\wirtualizzcje\lab\lab08\breach-checker>
```

Oba tagi mają ten sam digest, więc wskazują tę samą zawartość. Pull działa bez logowania, bo pakiet jest publiczny, a zapis wymaga uwierzytelnienia. Push latest nie zgłosił błędu, bo w rejestrze był już identyczny obraz z tym tagiem i nic nie zostało zapisane, natomiast zapis nowego tagu został odrzucony. Token z zakresem write:packages służył do ręcznej publikacji obrazu w kroku 1.
