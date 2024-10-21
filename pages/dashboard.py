import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.auth_utils import load_projects, apply_custom_style_and_header
import os

def set_user_info(user_id, user_email):
    st.session_state['current_user_id'] = user_id
    st.session_state['current_user_email'] = user_email

def app():
    apply_custom_style_and_header("Dashboard")
    
    # Exibir as informações do usuário na página
    st.write(f"Bem-vindo, {st.session_state.get('current_user_email', 'Usuário')}")
    
    df = load_projects()
    
    if 'user_id' in df.columns and st.session_state.get('current_user_id'):
        df = df[df['user_id'] == st.session_state.get('current_user_id')]
        
        total_projects = len(df)
        st.metric("Total de Projetos", total_projects)

        total_hh_real = df['HH Real'].sum()
        st.metric("Total de HH Real", total_hh_real)

        # Exemplo de gráfico simples
        fig, ax = plt.subplots()
        df['Prioridade'].value_counts().plot(kind='bar', ax=ax)
        st.pyplot(fig)
    else:
        st.write("Erro: `user_id` não encontrado no DataFrame ou `current_user_id` não definido.")
