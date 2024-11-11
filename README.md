# 5Cloud

## Installation

```bash
# Création environnement virtuel & activation
python3 -m venv airflow_env
.\airflow_env\Scripts\activate
# Installation librairies listées dans 'requirements.txt'
pip install -r requirements.txt
pip freeze

## Télécharger le fichier docker-compose.yaml
Invoke-WebRequest -Uri 'https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml' -OutFile 'docker-compose.yaml'

## Initialiser la base de données Airflow
docker compose up airflow-init

## Démarrer les conteneurs
docker compose up

# Lancer jupyter
jupyter notebook
```