import streamlit as st
from utils.db import read_parquet

def show():
    st.title("Dashboard")
    
    st.header(f"Bem-vindo, {st.session_state.user_email}")
    
    st.subheader("Projetos")
    projects_df = read_parquet("projects")
    st.dataframe(projects_df)
    
    st.subheader("Tarefas")
    tasks_df = read_parquet("tasks")
    st.dataframe(tasks_df)

if __name__ == "__main__":
    show()
