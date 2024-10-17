import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import load_projects

def dashboard():
    st.title("Dashboard")

    df = load_projects()

    total_projects = len(df)
    st.metric("Total de Projetos", total_projects)
    
    total_hh_real = df['HH Real'].sum()
    st.metric("Total de HH Real", total_hh_real)
    
    # Exemplo de gráfico simples
    fig, ax = plt.subplots()
    df['Prioridade'].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)
