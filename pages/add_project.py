# pages/add_project.py
import streamlit as st
from database.db_operations import add_project

def show():
    st.header("Adicionar Novo Projeto")
    with st.form("novo_projeto"):
        new_project = {}
        new_project['projeto'] = st.text_input("Projeto")
        new_project['solicitante'] = st.text_input("Solicitante")
        new_project['responsavel'] = st.text_input("Responsável")
        new_project['atividade_principal'] = st.text_input("Atividade Principal")
        new_project['subatividade'] = st.text_input("Subatividade")
        new_project['data_prevista_inicio'] = st.date_input("Data Prevista de Início").isoformat()
        new_project['data_prevista_termino'] = st.date_input("Data Prevista de Término").isoformat()
        new_project['data_inicio_real'] = st.date_input("Data de Início Real").isoformat()
        new_project['data_termino_real'] = st.date_input("Data de Término Real").isoformat()
        new_project['hh_previsto'] = st.number_input("HH Previsto", min_value=0.0)
        new_project['hh_real'] = st.number_input("HH Real", min_value=0.0)
        new_project['ferramenta'] = st.text_input("Ferramenta")
        new_project['prioridade'] = st.selectbox("Prioridade", ["Baixa", "Média", "Alta"])
        
        if st.form_submit_button("Adicionar Projeto"):
            add_project(new_project)
            st.success("Projeto adicionado com sucesso!")