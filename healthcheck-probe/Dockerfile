FROM alpine
RUN apk add --no-cache curl
CMD ["sh", "-c", "if curl -fs http://backend:5000/health > /dev/null 2>&1; then echo 'backend: OK'; else echo 'backend: UNREACHABLE'; fi"]

