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

## Créer les répertoires 
mkdir -p dags logs plugins

## Initialiser la base de données Airflow
docker compose up airflow-init

## Démarrer les conteneurs
docker compose up

# Lancer jupyter
jupyter notebook
```
## Ingestion des Données avec Airflow
**Fichier** : `dags/process_paris_wifi.py`

**Description** : Ce DAG utilise une tâche PythonOperator pour récupérer les données de l'API de Paris Open Data.  
Airflow exécute cette tâche toutes les heures pour télécharger les données à jour.

**URL de l'API** : [https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/sites-disposant-du-service-paris-wi-fi/exports/csv?delimiter=%3B&quote_all=true&with_bom=true](https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/sites-disposant-du-service-paris-wi-fi/exports/csv?delimiter=%3B&quote_all=true&with_bom=true)  

**Technologie utilisée** : Le module `requests` pour faire une requête GET et sauvegarder le fichier CSV localement dans le dossier `dags/files/`.

## Transformation des Données avec Pandas

**Fichier** : `transform_data.py`

**Description** : Ce script nettoie et transforme les données pour les préparer à l'analyse. Les étapes de transformation incluent :

- **Suppression de colonnes** : Suppression de la colonne `geo_shape`.
- **Séparation des Coordonnées** : La colonne `geo_point_2d` est séparée en `latitude` et `longitude`.
- **Changement des Types de Données** : Changement des types de certaines colonnes pour garantir la cohérence (ex : `cp` en `string`).
- **Renommage des Colonnes** : Renommage de certaines colonnes pour simplifier leur utilisation dans les visualisations et sauvegarder le fichier CSV localement dans le dossier `data`.

## Visualisation des Données avec Jupyter Notebook et Plotly

**Fichier** : `notebooks/dashboard.ipynb`

**Description** : Ce notebook utilise `Plotly` et `Panel` pour créer des visualisations interactives. Les visualisations incluent :

- **Nombre de Points Wi-Fi par Adresse** : Un graphique à barres affichant le nombre de points Wi-Fi pour chaque adresse.
- **Nombre de Points Wi-Fi par Code Postal** : Un graphique à barres montrant la répartition des points Wi-Fi par code postal.
- **Carte des Points Wi-Fi** : Une carte interactive montrant les emplacements des points Wi-Fi.
- **Nombre de Bornes Wi-Fi par État et par Code Postal** : Un graphique qui montre le statut des bornes (ex : en service ou non) par code postal.

**Mise à jour et sauvegarde des tableaux de bord** :
- Les tableaux de bord sont mis à jour toutes les cinq minutes.
- Chaque visualisation est sauvegardée dans le répertoire `plots`, avec un horodatage dans le nom de fichier pour les différencier.
- Pour maintenir les mises à jour, il est nécessaire de laisser le terminal où Jupyter est lancé en marche.

