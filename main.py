# [START import_modules]
from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.models import PythonOperator

# [END import_modules]

# [START define_args]
default_args = {
    'owner': 'Cristiano o. da Silva',
    'depends_on_past': False,
    'start_date': datetime(2022, 8, 21),
    'email': ['crisosilva88@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': '@daily'
}
# [END define_args]

# [START instantiate_dag]
dag = DAG(
    'nba-data-analysis',
    default_args=default_args,
)
# [END instantiate_dag]

# [START tasks]
s3_sensor = S3KeySensor(
    task_id="s3_sensor",
    bucket_name= BUCKET_NAME,
    bucket_key=KEY,
)
# [END tasks]

# [START flow_tasks]

# [END flow_tasks]