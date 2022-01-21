# MY OWN COMMENTS
from datetime import datetime
from typing import Sequence

from airflow.models import DAG
from airflow.operators.dummy import DummyOperator

DEFAULT_DATE = datetime(2016, 1, 1)

default_args = {
    "owner": "airflow",
    "start_date": DEFAULT_DATE,
}

dag = DAG(dag_id="rogue_dag", default_args=default_args, schedule_interval='@once')


class MyDummyOperator(DummyOperator):
    template_fields_renderers = {"body": "json"}
    template_fields: Sequence[str] = ("body",)

    def __init__(self, body, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.body = body


with dag:
    task_a = DummyOperator(task_id="test_task_a")

    task_b = DummyOperator(task_id="test_task_b")

    task_a >> task_b

    task_c = MyDummyOperator(task_id="test_task_c", body={"hello": "world"})

    task_d = DummyOperator(task_id="test_task_on_execute", on_execute_callback=lambda *args, **kwargs: 1)

    task_e = DummyOperator(task_id="test_task_on_success", on_success_callback=lambda *args, **kwargs: 1)