from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests

def fetch_data():
    response = requests.get("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/sites-disposant-du-service-paris-wi-fi/exports/csv?delimiter=%3B&quote_all=true&with_bom=true")
    with open('/opt/airflow/dags/files/paris_wifi.csv', 'w') as file:
        file.write(response.text)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('data_ingestion', default_args=default_args, schedule_interval='@hourly')

fetch_data_task = PythonOperator(
    task_id='fetch_data',
    python_callable=fetch_data,
    dag=dag,
)