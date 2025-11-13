FROM python:3.11-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar solo requirements primero (para aprovechar cache de Docker)
COPY requirements.txt ./

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Puerto donde escucha Flask
EXPOSE 5000

# Comando de inicio
CMD ["python", "app.py"]
