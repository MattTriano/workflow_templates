from datetime import datetime

# from airflow.decorators import dag, task

# @dag(
#     schedule_interval=None,
#     start_date=datetime(2021, 1, 1),
#     catchup=False, tags=['chicago']
# )
# def chicago_boundary_etl():
#     """
#     ### TaskFlow API Tutorial Documentation
#     This is a simple ETL data pipeline example which demonstrates the use of
#     the TaskFlow API using three simple tasks for Extract, Transform, and Load.
#     Documentation that goes along with the Airflow TaskFlow API tutorial is
#     located
#     [here](https://airflow.apache.org/docs/apache-airflow/stable/tutorial_taskflow_api.html)
#     """
#     @task.docker(
#         image='taskflow_etl/socrata', 
#         mounts=["/data_raw:/data"], 
#     )
#     def extract():
#         # from scripts.get_metadata import main
#         # import json
        
#         # main(table_id="ewy2-6yfk", output_dir_path="/data")
#         import os

#         print(os.listdir("."))

#     extract

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
    
with DAG(
   dag_id="chicago_boundary_etl",
   description="Gets metadata for the Chicago Boundary table on Socrata using Docker.",
   start_date=datetime(2022, 3, 1),
   end_date=datetime(2022, 5, 1),
   schedule_interval="@weekly",
) as dag:
    get_chicago_boundary_metadata = DockerOperator(
        task_id="get_chicago_boundary_metadata",
        image="taskflow_etl/socrata",
        command=[
            "get_metadata",
            "--table_id",
            "ewy2-6yfk",
            "--output_dir_path",
            "/data",
        ],
        # network_mode="taskflow_etl_network",
        # Note: this host path is on the HOST, not in the Airflow docker container.
        mounts=["/data_raw:/opt/airflow/data"],
    )

    get_chicago_boundary_metadata