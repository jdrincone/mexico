# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias
RUN pip install --no-cache-dir fastapi 'strawberry-graphql[fastapi]' sqlalchemy uvicorn[standard] pandas

# Copia el resto de los archivos de la aplicación al contenedor
COPY . .

# Expone el puerto de la aplicación
EXPOSE 8000

# Comando para iniciar el servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
