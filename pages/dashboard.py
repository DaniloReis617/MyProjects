# pages/dashboard.py

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from database.db_operations import get_projects
from utils.data_processing import (
    get_projects_by_priority,
    get_top_responsaveis,
    calculate_overall_efficiency,
    get_projects_ending_soon,
    get_overdue_projects,
    calculate_project_delay,
    calculate_hh_efficiency
)
import pandas as pd
from datetime import datetime

def show():
    st.header("Dashboard de Gestão de Projetos")
    df = get_projects()
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total de Projetos", len(df))
    with col2:
        overall_efficiency = calculate_overall_efficiency(df)
        st.metric("Eficiência Geral", f"{overall_efficiency:.2f}%")
    with col3:
        projects_ending_soon = len(get_projects_ending_soon(df))
        st.metric("Projetos Finalizando em 7 dias", projects_ending_soon)
    with col4:
        overdue_projects = len(get_overdue_projects(df))
        st.metric("Projetos Atrasados", overdue_projects)
    
    # Gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        projects_by_priority = get_projects_by_priority(df)
        fig_priority = px.bar(
            x=list(projects_by_priority.keys()),
            y=list(projects_by_priority.values()),
            title="Projetos por Prioridade",
            labels={'x': 'Prioridade', 'y': 'Número de Projetos'},
            color=list(projects_by_priority.keys()),
            color_discrete_map={'Baixa': 'green', 'Média': 'yellow', 'Alta': 'red'}
        )
        st.plotly_chart(fig_priority)
    
    with col2:
        top_responsaveis = get_top_responsaveis(df)
        fig_responsavel = px.pie(
            values=top_responsaveis.values,
            names=top_responsaveis.index,
            title="Top 5 Responsáveis por Número de Projetos"
        )
        st.plotly_chart(fig_responsavel)
    
    # Timeline de Projetos
    st.subheader("Timeline de Projetos")
    df['data_prevista_inicio'] = pd.to_datetime(df['data_prevista_inicio'])
    df['data_prevista_termino'] = pd.to_datetime(df['data_prevista_termino'])
    df = df.sort_values('data_prevista_inicio')
    
    fig_timeline = px.timeline(
        df, 
        x_start="data_prevista_inicio", 
        x_end="data_prevista_termino", 
        y="projeto",
        color="prioridade",
        title="Timeline dos Projetos",
        color_discrete_map={'Baixa': 'green', 'Média': 'yellow', 'Alta': 'red'}
    )
    fig_timeline.update_yaxes(categoryorder="total ascending")
    st.plotly_chart(fig_timeline)
    
    # Tabela de Projetos em Andamento
    st.subheader("Projetos em Andamento")
    projects_in_progress = df[df['data_termino_real'].isna()].sort_values('data_prevista_termino')
    projects_in_progress['Atraso (dias)'] = projects_in_progress.apply(
        lambda x: calculate_project_delay(x['data_prevista_termino'], datetime.now().strftime('%Y-%m-%d')), axis=1
    )
    projects_in_progress['Eficiência HH'] = projects_in_progress.apply(
        lambda x: calculate_hh_efficiency(x['hh_previsto'], x['hh_real']), axis=1
    )
    st.dataframe(projects_in_progress[['projeto', 'responsavel', 'data_prevista_termino', 'Atraso (dias)', 'Eficiência HH']])
    
    # Gráfico de Eficiência de HH por Projeto
    st.subheader("Eficiência de Horas-Homem por Projeto")
    df['Eficiência HH'] = df.apply(lambda x: calculate_hh_efficiency(x['hh_previsto'], x['hh_real']), axis=1)
    fig_efficiency = px.bar(
        df.sort_values('Eficiência HH', ascending=False),
        x='projeto',
        y='Eficiência HH',
        title="Eficiência de Horas-Homem por Projeto",
        labels={'projeto': 'Projeto', 'Eficiência HH': 'Eficiência (%)'},
        color='Eficiência HH',
        color_continuous_scale=[(0, "red"), (0.5, "yellow"), (1, "green")]
    )
    st.plotly_chart(fig_efficiency)