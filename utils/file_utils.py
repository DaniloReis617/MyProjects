import os
import pandas as pd

def initialize_data_files():
    """Verifica se os arquivos Parquet existem, caso contrário, os cria."""
    # Definindo os arquivos e seus DataFrames correspondentes
    files = {
        'data/users.parquet': pd.DataFrame(columns=['user_id', 'email', 'password', 'name', 'created_at']),
        'data/projetos.parquet': pd.DataFrame(columns=["Projeto", "Solicitante", "user_id", "Responsável", "Atividade Principal", "Subatividade", 
                                   "Data Prevista de Início", "Data Prevista de Término", "Data de Início Real", 
                                   "Data de Término Real", "HH Previsto", "HH Real", "Ferramenta", "Prioridade"]),

    }

    # Verificar se os arquivos existem, se não, criar e salvar os DataFrames
    for file_path, df in files.items():
        if not os.path.exists(file_path):
            df.to_parquet(file_path)

if __name__ == "__main__":
    initialize_data_files()