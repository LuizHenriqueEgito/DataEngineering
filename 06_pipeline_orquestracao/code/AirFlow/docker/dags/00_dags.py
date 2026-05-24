from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator # type: ignore


def task_hello():
    print("Airflow está funcionando corretamente!")


def task_second():
    print("Segunda task executada com sucesso!")


with DAG(
    dag_id="teste_simples",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["teste"],
) as dag:

    t1 = PythonOperator(
        task_id="hello_task",
        python_callable=task_hello,
    )

    t2 = PythonOperator(
        task_id="second_task",
        python_callable=task_second,
    )

    t1 >> t2