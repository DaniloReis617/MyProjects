import streamlit as st
from utils.db import read_parquet, delete_record

def show():
    st.title("Deletar Item")
    
    st.header("Deletar Projeto")
    projects_df = read_parquet("projects")
    project_id = st.selectbox("Selecione o Projeto", projects_df["project_id"])
    
    if st.button("Deletar Projeto"):
        delete_record("projects", project_id)
        st.success("Projeto deletado com sucesso!")
    
    st.header("Deletar Tarefa")
    tasks_df = read_parquet("tasks")
    task_id = st.selectbox("Selecione a Tarefa", tasks_df["task_id"])
    
    if st.button("Deletar Tarefa"):
        delete_record("tasks", task_id)
        st.success("Tarefa deletada com sucesso!")

if __name__ == "__main__":
    show()
import streamlit as st
from utils.db import read_parquet, delete_record

def show():
    st.title("Deletar Item")
    
    st.header("Deletar Projeto")
    projects_df = read_parquet("projects")
    project_id = st.selectbox("Selecione o Projeto", projects_df["project_id"])
    
    if st.button("Deletar Projeto"):
        delete_record("projects", project_id)
        st.success("Projeto deletado com sucesso!")
    
    st.header("Deletar Tarefa")
    tasks_df = read_parquet("tasks")
    task_id = st.selectbox("Selecione a Tarefa", tasks_df["task_id"])
    
    if st.button("Deletar Tarefa"):
        delete_record("tasks", task_id)
        st.success("Tarefa deletada com sucesso!")

if __name__ == "__main__":
    show()
