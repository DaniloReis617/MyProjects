# database/db_operations.py
import sqlite3
import pandas as pd

DB_NAME = 'projetos.db'

def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS projetos (
        id INTEGER PRIMARY KEY,
        projeto TEXT,
        solicitante TEXT,
        responsavel TEXT,
        atividade_principal TEXT,
        subatividade TEXT,
        data_prevista_inicio TEXT,
        data_prevista_termino TEXT,
        data_inicio_real TEXT,
        data_termino_real TEXT,
        hh_previsto REAL,
        hh_real REAL,
        ferramenta TEXT,
        prioridade TEXT
    )
    ''')
    conn.commit()
    conn.close()

def add_project(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO projetos (projeto, solicitante, responsavel, atividade_principal, subatividade,
                          data_prevista_inicio, data_prevista_termino, data_inicio_real,
                          data_termino_real, hh_previsto, hh_real, ferramenta, prioridade)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', tuple(data.values()))
    conn.commit()
    conn.close()

def get_projects():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM projetos", conn)
    conn.close()
    return df

def update_project(id, data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE projetos
    SET projeto=?, solicitante=?, responsavel=?, atividade_principal=?, subatividade=?,
        data_prevista_inicio=?, data_prevista_termino=?, data_inicio_real=?,
        data_termino_real=?, hh_previsto=?, hh_real=?, ferramenta=?, prioridade=?
    WHERE id=?
    ''', tuple(data.values()) + (id,))
    conn.commit()
    conn.close()

def delete_project(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projetos WHERE id=?", (id,))
    conn.commit()
    conn.close()

# pages/home.py
import streamlit as st

def show():
    st.title("Bem-vindo ao Sistema de Gestão de Projetos")
    st.write("Use o menu lateral para navegar pelo sistema.")