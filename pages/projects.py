# pages/projects.py
import streamlit as st
from database.db_operations import get_projects, delete_project, update_project

def show():
    st.header("Lista de Projetos")
    df = get_projects()
    st.dataframe(df)
    
    project_id = st.number_input("ID do projeto para editar/excluir", min_value=1, step=1)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Editar"):
            project = df[df['id'] == project_id].iloc[0]
            edit_project(project)
    
    with col2:
        if st.button("Excluir"):
            delete_project(project_id)
            st.success(f"Projeto {project_id} excluído com sucesso!")
            st.experimental_rerun()

def edit_project(project):
    with st.form("editar_projeto"):
        new_data = {}
        for col in project.index:
            if col != 'id':
                new_data[col] = st.text_input(col, project[col])
        
        if st.form_submit_button("Atualizar Projeto"):
            update_project(project['id'], new_data)
            st.success("Projeto atualizado com sucesso!")
            st.experimental_rerun()