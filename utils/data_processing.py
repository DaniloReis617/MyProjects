# utils/data_processing.py

import pandas as pd
from datetime import datetime, timedelta

def calculate_project_duration(start_date, end_date):
    """
    Calcula a duração do projeto em dias.
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    return (end - start).days

def calculate_project_delay(planned_end_date, actual_end_date):
    """
    Calcula o atraso do projeto em dias.
    """
    planned = datetime.strptime(planned_end_date, "%Y-%m-%d")
    actual = datetime.strptime(actual_end_date, "%Y-%m-%d")
    delay = (actual - planned).days
    return max(0, delay)  # Retorna 0 se o projeto foi concluído antes do prazo

def calculate_hh_efficiency(hh_planned, hh_actual):
    """
    Calcula a eficiência de horas-homem (HH).
    """
    if hh_planned == 0:
        return 0
    return (hh_planned / hh_actual) * 100 if hh_actual > 0 else 100

def get_project_status(planned_end_date, actual_end_date=None):
    """
    Determina o status do projeto: 'Em andamento', 'Concluído' ou 'Atrasado'.
    """
    today = datetime.now().date()
    planned_end = datetime.strptime(planned_end_date, "%Y-%m-%d").date()
    
    if actual_end_date:
        actual_end = datetime.strptime(actual_end_date, "%Y-%m-%d").date()
        return "Concluído" if actual_end <= planned_end else "Concluído com atraso"
    else:
        return "Em andamento" if today <= planned_end else "Atrasado"

def format_date(date_string):
    """
    Formata a data para o formato dd/mm/yyyy.
    """
    date = datetime.strptime(date_string, "%Y-%m-%d")
    return date.strftime("%d/%m/%Y")

def get_projects_by_priority(df):
    """
    Retorna um dicionário com o número de projetos por prioridade.
    """
    return df['prioridade'].value_counts().to_dict()

def get_top_responsaveis(df, top_n=5):
    """
    Retorna os top N responsáveis com mais projetos.
    """
    return df['responsavel'].value_counts().nlargest(top_n)

def calculate_overall_efficiency(df):
    """
    Calcula a eficiência geral de todos os projetos.
    """
    total_hh_planned = df['hh_previsto'].sum()
    total_hh_actual = df['hh_real'].sum()
    return calculate_hh_efficiency(total_hh_planned, total_hh_actual)

def get_projects_ending_soon(df, days=7):
    """
    Retorna projetos que estão próximos da data de conclusão prevista.
    """
    today = datetime.now().date()
    end_date = today + timedelta(days=days)
    mask = (df['data_prevista_termino'] > today.isoformat()) & (df['data_prevista_termino'] <= end_date.isoformat())
    return df[mask]

def get_overdue_projects(df):
    """
    Retorna projetos que estão atrasados.
    """
    today = datetime.now().date()
    return df[df['data_prevista_termino'] < today.isoformat()]
