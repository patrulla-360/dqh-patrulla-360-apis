# Imagen base
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente al contenedor
COPY . .

# Exponer el puerto 8080
EXPOSE 8080

# Comando para ejecutar la API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
