import streamlit as st
from utils.db import add_record

def show():
    st.title("Criar Novo Item")
    
    st.header("Novo Projeto")
    project_name = st.text_input("Nome do Projeto")
    description = st.text_area("Descrição")
    start_date = st.date_input("Data de Início")
    end_date = st.date_input("Data de Término")
    
    if st.button("Criar Projeto"):
        new_project = {
            "project_name": project_name,
            "description": description,
            "start_date": start_date,
            "end_date": end_date
        }
        add_record("projects", new_project)
        st.success("Projeto criado com sucesso!")
    
    st.header("Nova Tarefa")
    task_name = st.text_input("Nome da Tarefa")
    project_id = st.number_input("ID do Projeto", min_value=1)
    assigned_to = st.text_input("Atribuído a")
    status = st.selectbox("Status", ["To Do", "In Progress", "Done"])
    due_date = st.date_input("Data de Vencimento")
    
    if st.button("Criar Tarefa"):
        new_task = {
            "task_name": task_name,
            "project_id": project_id,
            "assigned_to": assigned_to,
            "status": status,
            "due_date": due_date
        }
        add_record("tasks", new_task)
        st.success("Tarefa criada com sucesso!")

if __name__ == "__main__":
    show()
