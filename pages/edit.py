import streamlit as st
from utils.db import read_parquet, update_record
import pandas as pd

def show():
    st.title("Editar Item")
    
    st.header("Editar Projeto")
    projects_df = read_parquet("projects")
    project_id = st.selectbox("Selecione o Projeto", projects_df["project_id"])
    project = projects_df[projects_df["project_id"] == project_id].iloc
    
    project_name = st.text_input("Nome do Projeto", value=project["project_name"])
    description = st.text_area("Descrição", value=project["description"])
    start_date = st.date_input("Data de Início", value=pd.to_datetime(project["start_date"]))
    end_date = st.date_input("Data de Término", value=pd.to_datetime(project["end_date"]))
    
    if st.button("Atualizar Projeto"):
        updated_project = {
            "project_id": project_id,
            "project_name": project_name,
            "description": description,
            "start_date": start_date,
            "end_date": end_date
        }
        update_record("projects", project_id, updated_project)
        st.success("Projeto atualizado com sucesso!")
    
    st.header("Editar Tarefa")
    tasks_df = read_parquet("tasks")
    task_id = st.selectbox("Selecione a Tarefa", tasks_df["task_id"])
    task = tasks_df[tasks_df["task_id"] == task_id].iloc
    
    task_name = st.text_input("Nome da Tarefa", value=task["task_name"])
    project_id = st.number_input("ID do Projeto", min_value=1, value=task["project_id"])
    assigned_to = st.text_input("Atribuído a", value=task["assigned_to"])
    status = st.selectbox("Status", ["To Do", "In Progress", "Done"], index=["To Do", "In Progress", "Done"].index(task["status"]))
    due_date = st.date_input("Data de Vencimento", value=pd.to_datetime(task["due_date"]))
    
    if st.button("Atualizar Tarefa"):
        updated_task = {
            "task_id": task_id,
            "project_id": project_id,
            "task_name": task_name,
            "assigned_to": assigned_to,
            "status": status,
            "due_date": due_date
        }
        update_record("tasks", task_id, updated_task)
        st.success("Tarefa atualizada com sucesso!")

if __name__ == "__main__":
    show()
