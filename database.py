import pandas as pd
import os

parquet_file = 'data/projetos.parquet'

# Função para inicializar o arquivo Parquet
def init_parquet():
    if not os.path.exists(parquet_file):
        df = pd.DataFrame(columns=["Projeto", "Solicitante", "Responsável", "Atividade Principal", "Subatividade", 
                                   "Data Prevista de Início", "Data Prevista de Término", "Data de Início Real", 
                                   "Data de Término Real", "HH Previsto", "HH Real", "Ferramenta", "Prioridade"])
        df.to_parquet(parquet_file, index=False)

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
