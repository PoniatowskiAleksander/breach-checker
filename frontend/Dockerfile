# --- Etap 1: kontrola jakości HTML (narzędzia potrzebne tylko podczas budowania) ---
FROM node:24-alpine AS lint
RUN npm install -g htmlhint@1.9.2
WORKDIR /site
COPY index.html style.css script.js ./
RUN htmlhint index.html

# --- Etap 2: obraz końcowy - sam nginx i pliki strony ---
FROM nginx:alpine
LABEL maintainer="aleksande.poniatowski@student.put.poznan.pl"
COPY --from=lint /site/ /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
