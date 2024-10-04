import streamlit as st
from utils.db import read_parquet

def show():
    st.title("Tabela de Dados")
    
    st.header("Projetos")
    projects_df = read_parquet("projects")
    st.dataframe(projects_df)
    
    st.header("Tarefas")
    tasks_df = read_parquet("tasks")
    st.dataframe(tasks_df)

if __name__ == "__main__":
    show()
