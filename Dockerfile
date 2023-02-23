# Image python 3.11 sur la distribution alpine
FROM python:3.11-alpine
# Définition du working directory
WORKDIR /app/
# Copie des fichiers source
COPY ./api/ ./
# Copie du fichier d'initialisation de la base
COPY ./init_db.sql ./
# Installation des dépendances
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# Exposition du port de l'API
EXPOSE 5000
# Commande du lancement du serveur lors du démarrage du conteneur
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]