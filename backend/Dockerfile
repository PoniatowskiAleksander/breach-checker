FROM python:3.12-slim
WORKDIR /app

# 1. skopiuj do obrazu plik requirements.txt
COPY requirements.txt .
# 2. zainstaluj zależności: pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 3. skopiuj do obrazu plik app.py
COPY app.py .

EXPOSE 5000
CMD ["python", "app.py"]




# najpierw instalacja potem copy bo copy resetuje cache a nie chcemy pobierac za kazdym razem