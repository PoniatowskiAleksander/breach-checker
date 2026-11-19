PS C:\studia\sem3\wirtualizzcje\lab\lab07\breach-checker> docker compose -f docker-compose.yml up -d --build
[+] Building 8.6s (28/28) FINISHED                                                                                                                                      
 => [internal] load local bake definitions                                                                                                                         0.0s
 => => reading from stdin 1.14kB                                                                                                                                   0.0s
 => [frontend internal] load build definition from Dockerfile                                                                                                      0.2s
 => => transferring dockerfile: 525B                                                                                                                               0.1s
 => [backend internal] load build definition from Dockerfile                                                                                                       0.2s
 => => transferring dockerfile: 502B                                                                                                                               0.1s
 => [backend internal] load metadata for docker.io/library/python:3.12-slim                                                                                        3.0s
 => [frontend internal] load metadata for docker.io/library/nginx:alpine                                                                                           0.3s
 => [frontend internal] load metadata for docker.io/library/node:24-alpine                                                                                         2.7s
 => [frontend internal] load .dockerignore                                                                                                                         0.1s
 => => transferring context: 68B                                                                                                                                   0.0s
 => [frontend lint 1/5] FROM docker.io/library/node:24-alpine@sha256:116b800c3754b440ee0aa3ed2f20f5bf3d99a554bfd9adeea09ea8017f6e85f5                              0.2s
 => => resolve docker.io/library/node:24-alpine@sha256:116b800c3754b440ee0aa3ed2f20f5bf3d99a554bfd9adeea09ea8017f6e85f5                                            0.1s
 => [frontend stage-1 1/3] FROM docker.io/library/nginx:alpine@sha256:df221db836e1754089190208cee7eeda94f233197056426eda74a43ab1abeac2                             0.2s
 => => resolve docker.io/library/nginx:alpine@sha256:df221db836e1754089190208cee7eeda94f233197056426eda74a43ab1abeac2                                              0.2s
 => [frontend internal] load build context                                                                                                                         0.1s
 => => transferring context: 120B                                                                                                                                  0.0s
 => [backend internal] load .dockerignore                                                                                                                          0.1s
 => => transferring context: 192B                                                                                                                                  0.1s
 => CACHED [frontend lint 2/5] RUN npm install -g htmlhint@1.9.2                                                                                                   0.0s
 => CACHED [frontend lint 3/5] WORKDIR /site                                                                                                                       0.0s
 => CACHED [frontend lint 4/5] COPY index.html style.css script.js ./                                                                                              0.0s
 => CACHED [frontend lint 5/5] RUN htmlhint index.html                                                                                                             0.0s
 => CACHED [frontend stage-1 2/3] COPY --from=lint /site/ /usr/share/nginx/html/                                                                                   0.0s
 => CACHED [frontend stage-1 3/3] COPY nginx.conf /etc/nginx/conf.d/default.conf                                                                                   0.0s
 => [frontend] exporting to image                                                                                                                                  0.6s
 => => exporting layers                                                                                                                                            0.0s
 => => exporting manifest sha256:1e29f0002a529f852ad8a3215a195d79bde4a2d3b415da203b81dacd598041e5                                                                  0.0s
 => => exporting config sha256:8e1e73cb4762053f84c4ee903fd318cce6d89a4c716910157237007b30810f17                                                                    0.0s
 => => exporting attestation manifest sha256:5d8f90f77303c1fb6e88a5c0b4037ce6831bbc70d0fb13d7baa9d4d09c0c1504                                                      0.1s
 => => exporting manifest list sha256:66b202438fc35e7c3bbab653332565215e562fbb99356e010990287b7d92b654                                                             0.1s
 => => naming to docker.io/library/breach-checker-frontend:latest                                                                                                  0.0s
 => => unpacking to docker.io/library/breach-checker-frontend:latest                                                                                               0.1s
 => [backend 1/6] FROM docker.io/library/python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b                                  0.2s
 => => resolve docker.io/library/python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b                                          0.2s
 => [backend internal] load build context                                                                                                                          0.1s
 => => transferring context: 63B                                                                                                                                   0.0s
 => CACHED [backend 2/6] RUN useradd --system --no-create-home appuser                                                                                             0.0s
 => CACHED [backend 3/6] WORKDIR /app                                                                                                                              0.0s
 => CACHED [backend 4/6] COPY requirements.txt .                                                                                                                   0.0s
 => CACHED [backend 5/6] RUN pip install --no-cache-dir -r requirements.txt                                                                                        0.0s
 => CACHED [backend 6/6] COPY app.py .                                                                                                                             0.0s
 => [backend] exporting to image                                                                                                                                   1.0s
 => => exporting layers                                                                                                                                            0.0s
 => => exporting manifest sha256:72e2beeb9a642a3ee1f6c5c1c097f4e936a304e58c5ff884b34bba9884f76901                                                                  0.1s
 => => exporting config sha256:0468e98d35fcd1e4bbb6027329611710d6a3559ab4587831713f09fe2cbf6340                                                                    0.0s
 => => exporting attestation manifest sha256:78412a571d8d4ab5705d9fefdafc8a69e2e3c56c4f86c2bcd994269fa5bbc8b4                                                      0.1s
 => => exporting manifest list sha256:6a628d1d7ea32d50597b0800a1304c6343a28458a948e4a6fbc8b438b62d2e5f                                                             0.3s
 => => naming to docker.io/library/breach-checker-backend:latest                                                                                                   0.1s
 => => unpacking to docker.io/library/breach-checker-backend:latest                                                                                                0.1s
 => [frontend] resolving provenance for metadata file                                                                                                              0.2s
 => [backend] resolving provenance for metadata file                                                                                                               0.2s
[+] Running 5/5
 ✔ breach-checker-backend               Built                                                                                                                      0.0s 
 ✔ breach-checker-frontend              Built                                                                                                                      0.0s 
 ✘ Container breach-checker-backend-1   Error                                                                                                                     13.0s 
 ✔ Container breach-checker-frontend-1  Recreated                                                                                                                  1.1s 
 ✔ Container breach-checker-db-1        Healthy                                                                                                                    7.2s 
dependency failed to start: container breach-checker-backend-1 exited (255)
PS C:\studia\sem3\wirtualizzcje\lab\lab07\breach-checker> 
PS C:\studia\sem3\wirtualizzcje\lab\lab07\breach-checker> docker compose ps -a
>> 
NAME                        IMAGE                     COMMAND                  SERVICE    CREATED         STATUS                       PORTS
breach-checker-backend-1    breach-checker-backend    "gunicorn --bind 0.0…"   backend    5 minutes ago   Exited (255) 5 minutes ago   
breach-checker-db-1         postgres:16-alpine        "docker-entrypoint.s…"   db         6 days ago      Up 5 minutes (healthy)       5432/tcp
breach-checker-frontend-1   breach-checker-frontend   "/docker-entrypoint.…"   frontend   5 minutes ago   Created                      
PS C:\studia\sem3\wirtualizzcje\lab\lab07\breach-checker> docker compose logs backend
>> 
backend-1  | [2026-11-19 11:38:07 +0000] [1] [INFO] Starting gunicorn 26.2.0
backend-1  | [2026-11-19 11:38:07 +0000] [1] [INFO] Listening at: http://0.0.0.0:5000 (1)
backend-1  | [2026-11-19 11:38:07 +0000] [1] [INFO] Using worker: sync
backend-1  | [2026-11-19 11:38:07 +0000] [1] [ERROR] Unhandled exception in main loop
backend-1  | Traceback (most recent call last):
backend-1  |   File "/usr/local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 248, in run
backend-1  |     self.manage_workers()
backend-1  |   File "/usr/local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 701, in manage_workers
backend-1  |     self.spawn_workers()
backend-1  |   File "/usr/local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 788, in spawn_workers
backend-1  |     self.spawn_worker()
backend-1  |   File "/usr/local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 729, in spawn_worker
backend-1  |     worker = self.worker_class(self.worker_age, self.pid, self.LISTENERS,
backend-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
backend-1  |   File "/usr/local/lib/python3.12/site-packages/gunicorn/workers/base.py", line 66, in __init__
backend-1  |     self.tmp = WorkerTmp(cfg)
backend-1  |                ^^^^^^^^^^^^^^
backend-1  |   File "/usr/local/lib/python3.12/site-packages/gunicorn/workers/workertmp.py", line 23, in __init__
backend-1  |     fd, name = tempfile.mkstemp(prefix="wgunicorn-", dir=fdir)
backend-1  |                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
backend-1  |   File "/usr/local/lib/python3.12/tempfile.py", line 404, in mkstemp
backend-1  |     prefix, suffix, dir, output_type = _sanitize_params(prefix, suffix, dir)
backend-1  |                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
backend-1  |   File "/usr/local/lib/python3.12/tempfile.py", line 127, in _sanitize_params
backend-1  |     dir = gettempdir()
backend-1  |           ^^^^^^^^^^^^
backend-1  |   File "/usr/local/lib/python3.12/tempfile.py", line 369, in gettempdir
backend-1  |     return _os.fsdecode(_gettempdir())
backend-1  |                         ^^^^^^^^^^^^^
backend-1  |   File "/usr/local/lib/python3.12/tempfile.py", line 362, in _gettempdir
backend-1  |     tempdir = _get_default_tempdir()
backend-1  |               ^^^^^^^^^^^^^^^^^^^^^^
backend-1  |   File "/usr/local/lib/python3.12/tempfile.py", line 224, in _get_default_tempdir
backend-1  |     raise FileNotFoundError(_errno.ENOENT,
backend-1  | FileNotFoundError: [Errno 2] No usable temporary directory found in ['/tmp', '/var/tmp', '/usr/tmp', '/app']
PS C:\studia\sem3\wirtualizzcje\lab\lab07\breach-checker> Start-Transcript -Path terminal.txt
Transcript started, output file is terminal.txt
PS C:\studia\sem3\wirtualizzcje\lab\lab07\breach-checker> docker compose -f docker-compose.yml up -d --build
[+] Building 4.1s (28/28) FINISHED                                                                                                                                      
 => [internal] load local bake definitions                                                                                                                         0.0s
 => => reading from stdin 1.14kB                                                                                                                                   0.0s
 => [frontend internal] load build definition from Dockerfile                                                                                                      0.1s
 => => transferring dockerfile: 525B                                                                                                                               0.0s
 => [backend internal] load build definition from Dockerfile                                                                                                       0.1s
 => => transferring dockerfile: 502B                                                                                                                               0.0s
 => [frontend internal] load metadata for docker.io/library/node:24-alpine                                                                                         1.9s
 => [frontend internal] load metadata for docker.io/library/nginx:alpine                                                                                           0.1s
 => [backend internal] load metadata for docker.io/library/python:3.12-slim                                                                                        2.2s
 => [frontend internal] load .dockerignore                                                                                                                         0.0s
 => => transferring context: 68B                                                                                                                                   0.0s
 => [frontend lint 1/5] FROM docker.io/library/node:24-alpine@sha256:116b800c3754b440ee0aa3ed2f20f5bf3d99a554bfd9adeea09ea8017f6e85f5                              0.1s
 => => resolve docker.io/library/node:24-alpine@sha256:116b800c3754b440ee0aa3ed2f20f5bf3d99a554bfd9adeea09ea8017f6e85f5                                            0.1s
 => [frontend stage-1 1/3] FROM docker.io/library/nginx:alpine@sha256:df221db836e1754089190208cee7eeda94f233197056426eda74a43ab1abeac2                             0.1s
 => => resolve docker.io/library/nginx:alpine@sha256:df221db836e1754089190208cee7eeda94f233197056426eda74a43ab1abeac2                                              0.1s
 => [frontend internal] load build context                                                                                                                         0.0s
 => => transferring context: 120B                                                                                                                                  0.0s
 => CACHED [frontend lint 2/5] RUN npm install -g htmlhint@1.9.2                                                                                                   0.0s
 => CACHED [frontend lint 3/5] WORKDIR /site                                                                                                                       0.0s
 => CACHED [frontend lint 4/5] COPY index.html style.css script.js ./                                                                                              0.0s
 => CACHED [frontend lint 5/5] RUN htmlhint index.html                                                                                                             0.0s
 => CACHED [frontend stage-1 2/3] COPY --from=lint /site/ /usr/share/nginx/html/                                                                                   0.0s
 => CACHED [frontend stage-1 3/3] COPY nginx.conf /etc/nginx/conf.d/default.conf                                                                                   0.0s
 => [frontend] exporting to image                                                                                                                                  0.3s
 => => exporting layers                                                                                                                                            0.0s
 => => exporting manifest sha256:1e29f0002a529f852ad8a3215a195d79bde4a2d3b415da203b81dacd598041e5                                                                  0.0s
 => => exporting config sha256:8e1e73cb4762053f84c4ee903fd318cce6d89a4c716910157237007b30810f17                                                                    0.0s
 => => exporting attestation manifest sha256:7548378e1a3f740c067093c73318af7d718b6f74e6e81ee1dae18f5e151991ed                                                      0.0s
 => => exporting manifest list sha256:f05afff0e59ce4f8bcd9a5f8cc65ad86ffcdaa90ab6f6e0126cb474a8f16cfc4                                                             0.0s
 => => naming to docker.io/library/breach-checker-frontend:latest                                                                                                  0.0s
 => => unpacking to docker.io/library/breach-checker-frontend:latest                                                                                               0.0s
 => [backend internal] load .dockerignore                                                                                                                          0.0s
 => => transferring context: 192B                                                                                                                                  0.0s
 => [backend 1/6] FROM docker.io/library/python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b                                  0.1s
 => => resolve docker.io/library/python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b                                          0.1s
 => [backend internal] load build context                                                                                                                          0.0s
 => => transferring context: 63B                                                                                                                                   0.0s
 => CACHED [backend 2/6] RUN useradd --system --no-create-home appuser                                                                                             0.0s
 => CACHED [backend 3/6] WORKDIR /app                                                                                                                              0.0s
 => CACHED [backend 4/6] COPY requirements.txt .                                                                                                                   0.0s
 => CACHED [backend 5/6] RUN pip install --no-cache-dir -r requirements.txt                                                                                        0.0s
 => CACHED [backend 6/6] COPY app.py .                                                                                                                             0.0s
 => [backend] exporting to image                                                                                                                                   0.3s
 => => exporting layers                                                                                                                                            0.0s
 => => exporting manifest sha256:72e2beeb9a642a3ee1f6c5c1c097f4e936a304e58c5ff884b34bba9884f76901                                                                  0.0s
 => => exporting config sha256:0468e98d35fcd1e4bbb6027329611710d6a3559ab4587831713f09fe2cbf6340                                                                    0.0s
 => => exporting attestation manifest sha256:6e42c8266bf6589e05e006bc07741442592606b0d4069a2ffc7899518759fb17                                                      0.1s
 => => exporting manifest list sha256:ede831c24f8bd80ed671aaa1cedce2f48ba6b8b5259be3d27da4171974c8de6c                                                             0.0s
 => => naming to docker.io/library/breach-checker-backend:latest                                                                                                   0.0s
 => => unpacking to docker.io/library/breach-checker-backend:latest                                                                                                0.0s
 => [frontend] resolving provenance for metadata file                                                                                                              0.0s
 => [backend] resolving provenance for metadata file                                                                                                               0.0s
[+] Running 5/5
 ✔ breach-checker-frontend              Built                                                                                                                      0.0s 
 ✔ breach-checker-backend               Built                                                                                                                      0.0s 
 ✔ Container breach-checker-db-1        Healthy                                                                                                                    1.5s 
 ✔ Container breach-checker-backend-1   Healthy                                                                                                                    7.7s 
 ✔ Container breach-checker-frontend-1  Started                                                                                                                    7.8s 
PS C:\studia\sem3\wirtualizzcje\lab\lab07\breach-checker> 
PS C:\studia\sem3\wirtualizzcje\lab\lab07\breach-checker> docker compose exec backend touch /etc/test
>> 
touch: cannot touch '/etc/test': Read-only file system
PS C:\studia\sem3\wirtualizzcje\lab\lab07\breach-checker> docker compose exec backend touch /tmp/test
>> 
PS C:\studia\sem3\wirtualizzcje\lab\lab07\breach-checker> docker compose exec backend grep CapEff /proc/1/status
>> 
CapEff: 0000000000000000
PS C:\studia\sem3\wirtualizzcje\lab\lab07\breach-checker> docker compose up -d --build
>> 
[+] Building 6.1s (26/26) FINISHED                                                                                                                                      
 => [internal] load local bake definitions                                                                                                                         0.0s
 => => reading from stdin 1.14kB                                                                                                                                   0.0s
 => [backend internal] load build definition from Dockerfile.dev                                                                                                   0.1s
 => => transferring dockerfile: 390B                                                                                                                               0.0s
 => [frontend internal] load build definition from Dockerfile                                                                                                      0.0s
 => => transferring dockerfile: 525B                                                                                                                               0.0s
 => [frontend internal] load metadata for docker.io/library/nginx:alpine                                                                                           0.3s
 => [frontend internal] load metadata for docker.io/library/node:24-alpine                                                                                         1.9s
 => [backend internal] load metadata for docker.io/library/python:3.12-slim                                                                                        2.2s
 => [frontend internal] load .dockerignore                                                                                                                         0.0s
 => => transferring context: 68B                                                                                                                                   0.0s
 => [frontend stage-1 1/3] FROM docker.io/library/nginx:alpine@sha256:df221db836e1754089190208cee7eeda94f233197056426eda74a43ab1abeac2                             0.1s
 => => resolve docker.io/library/nginx:alpine@sha256:df221db836e1754089190208cee7eeda94f233197056426eda74a43ab1abeac2                                              0.1s
 => [frontend internal] load build context                                                                                                                         0.0s
 => => transferring context: 120B                                                                                                                                  0.0s
 => [frontend lint 1/5] FROM docker.io/library/node:24-alpine@sha256:116b800c3754b440ee0aa3ed2f20f5bf3d99a554bfd9adeea09ea8017f6e85f5                              0.1s
 => => resolve docker.io/library/node:24-alpine@sha256:116b800c3754b440ee0aa3ed2f20f5bf3d99a554bfd9adeea09ea8017f6e85f5                                            0.1s
 => CACHED [frontend lint 2/5] RUN npm install -g htmlhint@1.9.2                                                                                                   0.0s
 => CACHED [frontend lint 3/5] WORKDIR /site                                                                                                                       0.0s
 => CACHED [frontend lint 4/5] COPY index.html style.css script.js ./                                                                                              0.0s
 => CACHED [frontend lint 5/5] RUN htmlhint index.html                                                                                                             0.0s
 => CACHED [frontend stage-1 2/3] COPY --from=lint /site/ /usr/share/nginx/html/                                                                                   0.0s
 => CACHED [frontend stage-1 3/3] COPY nginx.conf /etc/nginx/conf.d/default.conf                                                                                   0.0s
 => [frontend] exporting to image                                                                                                                                  0.3s
 => => exporting layers                                                                                                                                            0.0s
 => => exporting manifest sha256:1e29f0002a529f852ad8a3215a195d79bde4a2d3b415da203b81dacd598041e5                                                                  0.0s
 => => exporting config sha256:8e1e73cb4762053f84c4ee903fd318cce6d89a4c716910157237007b30810f17                                                                    0.0s
 => => exporting attestation manifest sha256:a765be0aa63f9f5007628f40cff6d33ee075597e39b8e37dc7e9c41c7bc8afc2                                                      0.0s
 => => exporting manifest list sha256:225861b5416991ae2f6ff4312fcc8be920d09c6b6ddd8d6dafb0b8905bafa6ea                                                             0.0s
 => => naming to docker.io/library/breach-checker-frontend:latest                                                                                                  0.0s
 => => unpacking to docker.io/library/breach-checker-frontend:latest                                                                                               0.1s
 => [backend internal] load .dockerignore                                                                                                                          0.0s
 => => transferring context: 192B                                                                                                                                  0.0s
 => [backend 1/4] FROM docker.io/library/python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b                                  0.1s
 => => resolve docker.io/library/python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b                                          0.1s
 => [backend internal] load build context                                                                                                                          0.0s
 => => transferring context: 95B                                                                                                                                   0.0s
 => CACHED [backend 2/4] WORKDIR /app                                                                                                                              0.0s
 => CACHED [backend 3/4] COPY requirements.txt requirements-dev.txt ./                                                                                             0.0s
 => CACHED [backend 4/4] RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt                                                                0.0s
 => [backend] exporting to image                                                                                                                                   2.3s
 => => exporting layers                                                                                                                                            0.0s
 => => exporting manifest sha256:2f97a0ee403ccffd14369af4293692615524fbfb1746189c590e0736e77b8ccd                                                                  0.0s
 => => exporting config sha256:4411a23d53fb55d62f1b9d243d216699a855566edc5523b877ec66154399305d                                                                    0.0s
 => => exporting attestation manifest sha256:d00cc6351b5e0919d6e67ddd4154bcb92da26be820ac41af7e4dc588597b8ff6                                                      0.1s
 => => exporting manifest list sha256:49e7b84e2fabb45a8120a0c7c7c654c2b3889644673b8bd744f42be1179fdbff                                                             0.1s
 => => naming to docker.io/library/breach-checker-backend:latest                                                                                                   0.0s
 => => unpacking to docker.io/library/breach-checker-backend:latest                                                                                                2.0s
 => [frontend] resolving provenance for metadata file                                                                                                              0.0s
 => [backend] resolving provenance for metadata file                                                                                                               0.0s
[+] Running 5/5
 ✔ breach-checker-backend               Built                                                                                                                      0.0s 
 ✔ breach-checker-frontend              Built                                                                                                                      0.0s 
 ✔ Container breach-checker-db-1        Healthy                                                                                                                    3.5s 
 ✔ Container breach-checker-backend-1   Healthy                                                                                                                    9.4s 
 ✔ Container breach-checker-frontend-1  Started                                                                                                                    8.2s 
PS C:\studia\sem3\wirtualizzcje\lab\lab07\breach-checker> docker compose exec backend pytest
========================================================================= test session starts ==========================================================================
platform linux -- Python 3.12.16, pytest-8.4.2, pluggy-1.7.0
rootdir: /app
collected 7 items                                                                                                                                                      

tests/test_check.py .......                                                                                                                                      [100%]

========================================================================== 7 passed in 0.36s ===========================================================================
PS C:\studia\sem3\wirtualizzcje\lab\lab07\breach-checker> Stop-Transcript
Transcript stopped, output file is C:\studia\sem3\wirtualizzcje\lab\lab07\breach-checker\terminal.txt
PS C:\studia\sem3\wirtualizzcje\lab\lab07\breach-checker> 
















