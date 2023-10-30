from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

#instanciando a dag
dag = DAG('dagGroup', description="Dag group",
          schedule_interval=None,
          start_date=datetime(2023,3,5),
          catchup=False
          )

#tem que instanciar o task group, dando um nome e indicando qual a dag
tsk_group = TaskGroup("tsk_group", dag=dag)

task1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="tsk2", bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id="tsk3", bash_command="sleep 5", dag=dag)
task4 = BashOperator(task_id="tsk4", bash_command="sleep 5", dag=dag)
task5 = BashOperator(task_id="tsk5", bash_command="sleep 5", dag=dag)
task6 = BashOperator(task_id="tsk6", bash_command="sleep 5", dag=dag)

#comeca o task group
task7 = BashOperator(task_id="tsk7", bash_command="sleep 5", dag=dag,task_group=tsk_group)
task8 = BashOperator(task_id="tsk8", bash_command="sleep 5", dag=dag,task_group=tsk_group)
task9 = BashOperator(task_id="tsk9", bash_command="sleep 5", dag=dag,task_group=tsk_group,
                    trigger_rule='one_failed')


task1 >> task2
task3 >> task4
[task2,task4] >> task5
task5 >> task6
task6 >> tsk_group