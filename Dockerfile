# Temel Python imajı
FROM python:3.11-slim

# Ortam değişkeni
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Çalışma dizini
WORKDIR /app

# Bağımlılık dosyalarını kopyala
COPY requirements.txt /app/

# Sistem bağımlılıkları ve pip paketlerini kur
RUN apt-get update && apt-get install -y \
    gcc \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
 && pip install --upgrade pip \
 && pip install -r requirements.txt \
 && apt-get clean

# Uygulama dosyalarını kopyala
COPY . /app/

# Port
EXPOSE 5000

# Çalıştırılacak komut
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
