import streamlit as st
from database import load_projects, add_project, delete_project, edit_project
import pandas as pd

def crud_projects():
    st.title("Lista de Projetos")
    
    # Exibir os projetos
    df = load_projects()
    st.dataframe(df)

    # Adicionar novo projeto
    st.subheader("Adicionar novo projeto")
    with st.form("Projeto"):
        projeto = st.text_input("Projeto")
        solicitante = st.text_input("Solicitante")
        responsavel = st.text_input("Responsável")
        atividade_principal = st.text_input("Atividade Principal")
        subatividade = st.text_input("Subatividade")
        data_prev_inicio = st.date_input("Data Prevista de Início")
        data_prev_termino = st.date_input("Data Prevista de Término")
        data_inicio_real = st.date_input("Data de Início Real")
        data_termino_real = st.date_input("Data de Término Real")
        hh_previsto = st.number_input("HH Previsto", min_value=0.0)
        hh_real = st.number_input("HH Real", min_value=0.0)
        ferramenta = st.text_input("Ferramenta")
        prioridade = st.selectbox("Prioridade", ["Baixa", "Média", "Alta"])
        submitted = st.form_submit_button("Adicionar")

        if submitted:
            add_project(projeto, solicitante, responsavel, atividade_principal, subatividade, data_prev_inicio, 
                        data_prev_termino, data_inicio_real, data_termino_real, hh_previsto, hh_real, ferramenta, prioridade)
            st.success("Projeto adicionado com sucesso!")

    # Deletar projeto
    st.subheader("Deletar Projeto")
    project_index = st.number_input("Índice do Projeto", min_value=0, max_value=len(df)-1, step=1)
    if st.button("Deletar"):
        delete_project(project_index)
        st.success("Projeto deletado com sucesso!")
