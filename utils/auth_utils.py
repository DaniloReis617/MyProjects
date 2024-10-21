import pandas as pd
import streamlit as st
import datetime
import hashlib
import os
import re

USERS_FILE = 'data/users.parquet'
parquet_file = 'data/projetos.parquet'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email)

def authenticate_user(email, password):
    """Autentica um usuário com base no email e senha."""
    if not os.path.exists(USERS_FILE):
        return False  # Não há usuários registrados
    
    users = pd.read_parquet(USERS_FILE)
    hashed_password = hash_password(password)
    
    user = users[(users['email'] == email) & (users['password'] == hashed_password)]
    return not user.empty

def get_user_by_email(email):
    """Retorna as informações do usuário pelo email."""
    if not os.path.exists(USERS_FILE):
        return None

    users = pd.read_parquet(USERS_FILE)
    user = users[users['email'] == email]

    if user.empty:
        return None

    return user.iloc[0]  # Retorna o primeiro usuário encontrado como um dicionário

def register_user(email, password):
    """Registra um novo usuário."""
    # Verificar formato do email
    if not is_valid_email(email):
        return False, "Email inválido."

    if not os.path.exists(USERS_FILE):
        users = pd.DataFrame(columns=['user_id', 'email', 'password'])
    else:
        users = pd.read_parquet(USERS_FILE)

    if email in users['email'].values:
        return False, "O email já está em uso."

    hashed_password = hash_password(password)
    
    new_user = pd.DataFrame({
        'user_id': [len(users) + 1],
        'email': [email],
        'password': [hashed_password]
    })
    
    updated_users = pd.concat([users, new_user], ignore_index=True)
    updated_users.to_parquet(USERS_FILE)

    return True, "Usuário registrado com sucesso."

def save_user_data(users_df):
    """Salva os dados de todos os usuários no arquivo Parquet."""
    users_df.to_parquet('data/users.parquet', index=False)

# Verifica se o arquivo Parquet existe e retorna um DataFrame vazio se não existir
def load_parquet_file(filepath, columns):
    if not os.path.exists(filepath):
        return pd.DataFrame(columns=columns)
    return pd.read_parquet(filepath)

def save_parquet_file(df, filepath):
    df.to_parquet(filepath)

# Funções para carregar dados
def get_user_data():
    """Retorna os dados dos usuários."""
    return load_parquet_file('data/users.parquet', ['user_id', 'email', 'password'])

# Função para carregar os projetos do arquivo Parquet
def load_projects():
    return pd.read_parquet(parquet_file)

# Função para salvar os projetos no arquivo Parquet
def save_projects(df):
    df.to_parquet(parquet_file, index=False)

# Função para adicionar um novo projeto
def add_project(projeto, solicitante, responsavel, atividade_principal, subatividade, data_prev_inicio, 
                data_prev_termino, data_inicio_real, data_termino_real, hh_previsto, hh_real, ferramenta, prioridade):
    df = load_projects()
    new_project = pd.DataFrame({
        "Projeto": [projeto],
        "Solicitante": [solicitante],
        "Responsável": [responsavel],
        "Atividade Principal": [atividade_principal],
        "Subatividade": [subatividade],
        "Data Prevista de Início": [data_prev_inicio],
        "Data Prevista de Término": [data_prev_termino],
        "Data de Início Real": [data_inicio_real],
        "Data de Término Real": [data_termino_real],
        "HH Previsto": [hh_previsto],
        "HH Real": [hh_real],
        "Ferramenta": [ferramenta],
        "Prioridade": [prioridade]
    })
    df = pd.concat([df, new_project], ignore_index=True)
    save_projects(df)

# Função para deletar um projeto
def delete_project(index):
    df = load_projects()
    df = df.drop(index)
    save_projects(df)

# Função para editar um projeto
def edit_project(index, projeto, solicitante, responsavel, atividade_principal, subatividade, data_prev_inicio, 
                 data_prev_termino, data_inicio_real, data_termino_real, hh_previsto, hh_real, ferramenta, prioridade):
    df = load_projects()
    df.loc[index] = [projeto, solicitante, responsavel, atividade_principal, subatividade, data_prev_inicio, 
                     data_prev_termino, data_inicio_real, data_termino_real, hh_previsto, hh_real, ferramenta, prioridade]
    save_projects(df)

# Função para aplicar estilo customizado e criar o cabeçalho
def apply_custom_style_and_header(title):
    st.markdown("""
        <style>
        .main {
            background-color: white;  /* Cor de fundo padrão */
            color: black;  /* Texto em preto */
            font-family: Arial, sans-serif;
        }
        .stButton button {
            width: auto;
            padding: 5px 10px;
            background-color: #f44336;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 14px;
            border-radius: 5px;
        }
        .stButton button:hover {
            background-color: #e57373;
        }
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            background-color: white;
            border-bottom: 2px solid #f0f0f0;
            position: fixed;
            width: 100%;
            top: 0;
            left: 0;
            z-index: 1000;
        }
        .title-container {
            flex-grow: 1;
            text-align: left;
            padding-left: 240px; /* Ajuste para alinhar o título ao lado do sidebar */
        }
        .title-container h1 {
            font-size: 32px;
            font-weight: bold;
            color: black;
            font-family: Calibri, sans-serif;
            margin: 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabeçalho com título ao lado do sidebar
    st.markdown(f"""
        <div class="header-container">
            <div class="title-container">
                <h1>{title}</h1>
            </div>
            <div class="user-info">
                {get_user_info()}
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Criar um espaçamento para o conteúdo abaixo, já que o cabeçalho é fixo
    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

# Função para exibir o login, perfil do usuário e a hora atual
def get_user_info():
    if 'set_user_info' in st.session_state:
        user_login = st.session_state['set_user_info'].get('login', 'Usuário não identificado')
        user_id = st.session_state['set_user_info'].get('ID', 'ID não identificado')
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return f"<div style='text-align: right;'>Usuário: {user_login} ({user_id})<br>Data e Hora: {current_time}</div>"
    return ""