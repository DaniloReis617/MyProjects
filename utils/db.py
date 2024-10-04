import os
import pandas as pd

DATA_DIR = "Data"

FILES = {
    "users": ["username", "email", "password"],
    "projects": ["project_id", "project_name", "description", "start_date", "end_date"],
    "tasks": ["task_id", "project_id", "task_name", "assigned_to", "status", "due_date"]
}

def create_parquet_files():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    for file_name, columns in FILES.items():
        file_path = os.path.join(DATA_DIR, f"{file_name}.parquet")
        if not os.path.exists(file_path):
            df = pd.DataFrame(columns=columns)
            df.to_parquet(file_path)
            print(f"Arquivo {file_name}.parquet criado com sucesso.")
        else:
            print(f"Arquivo {file_name}.parquet já existe.")

def verify_parquet_files():
    for file_name, columns in FILES.items():
        file_path = os.path.join(DATA_DIR, f"{file_name}.parquet")
        if os.path.exists(file_path):
            df = pd.read_parquet(file_path)
            if not all(column in df.columns for column in columns):
                print(f"Arquivo {file_name}.parquet está faltando colunas.")
            else:
                print(f"Arquivo {file_name}.parquet verificado com sucesso.")
        else:
            print(f"Arquivo {file_name}.parquet não encontrado.")

def read_parquet(file_name):
    file_path = os.path.join(DATA_DIR, f"{file_name}.parquet")
    if os.path.exists(file_path):
        return pd.read_parquet(file_path)
    else:
        raise FileNotFoundError(f"O arquivo {file_name}.parquet não foi encontrado.")

def write_parquet(file_name, df):
    file_path = os.path.join(DATA_DIR, f"{file_name}.parquet")
    df.to_parquet(file_path)

def add_record(file_name, record):
    df = read_parquet(file_name)
    new_record_df = pd.DataFrame([record])
    df = pd.concat([df, new_record_df], ignore_index=True)
    write_parquet(file_name, df)

def update_record(file_name, index, updated_record):
    df = read_parquet(file_name)
    if index in df.index:
        df.loc[index] = updated_record
        write_parquet(file_name, df)
    else:
        raise IndexError(f"O índice {index} não existe no arquivo {file_name}.parquet.")

def delete_record(file_name, index):
    df = read_parquet(file_name)
    if index in df.index:
        df = df.drop(index)
        write_parquet(file_name, df)
    else:
        raise IndexError(f"O índice {index} não existe no arquivo {file_name}.parquet.")
