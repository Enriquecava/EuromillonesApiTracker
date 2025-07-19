# Usa imagen oficial de Python
FROM python:3.11-slim

# Instala dependencias del sistema necesarias para Playwright
RUN apt-get update && apt-get install -y \
    wget curl gnupg2 fonts-liberation xdg-utils \
    libnss3 libatk1.0-0 libatk-bridge2.0-0 libxcomposite1 \
    libxrandr2 libxdamage1 libgbm1 libasound2 libxshmfence1 \
    libxss1 libxtst6 libappindicator3-1 libu2f-udev libdrm2 \
    libvulkan1 ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia los requisitos e instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto
COPY . .

# Instala navegadores para Playwright
RUN python -m playwright install

# Expone el puerto 8000 que gunicorn usará
EXPOSE 8000

# Comando para iniciar la app Flask en producción
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
