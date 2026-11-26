FROM python:3.12-slim
LABEL org.opencontainers.image.source="https://github.com/<login-github>/breach-checker"
RUN useradd --system --no-create-home appuser
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
USER appuser
EXPOSE 5001
# Jeden proces wystarczy - usługa log ma mały ruch
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--workers", "1", "--no-control-socket", "app:app"]
