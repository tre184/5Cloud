from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pandas as pd

def change_column_types():
    df = pd.read_csv('/opt/airflow/dags/files/paris_wifi.csv', delimiter=';')

    # Drop the 'geo_shape' column
    df = df.drop(columns=['geo_shape'])

    # Function to separate geo_point_2d into longitude and latitude
    def separate_geo_point(geo_point):
        latitude, longitude = geo_point.split(', ')
        return pd.Series({'latitude': float(latitude), 'longitude': float(longitude)})

    # Apply the function to the 'geo_point_2d' column
    df[['latitude', 'longitude']] = df['geo_point_2d'].apply(separate_geo_point)

    # Drop the original 'geo_point_2d' column
    df = df.drop(columns=['geo_point_2d'])

    # Rename the column
    df = df.rename(columns={'etat2': 'etat'})
    df = df.rename(columns={'arc_adresse': 'adresse'})

    # Change the data types of the columns
    df = df.astype({
        'nom_site': 'string',
        'arc_adresse': 'string',
        'cp': 'string',
        'idpw': 'string',
        'nombre_de_borne_wifi': 'int',
        'etat': 'string'
    })
    # Save the modified DataFrame to a new CSV file
    df.to_csv('/opt/airflow/dags/data/paris_wifi_data.csv', index=False, sep=';')
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 11),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('data_transform', default_args=default_args, schedule_interval='@hourly')

change_column_types_task = PythonOperator(
    task_id='change_column_types',
    python_callable=change_column_types,
    dag=dag,
)
