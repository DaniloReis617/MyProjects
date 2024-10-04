import hashlib
import pandas as pd
from utils.db import read_parquet, add_record

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, email, password):
    users_df = read_parquet("users")
    if email in users_df["email"].values:
        raise ValueError("Email já registrado.")
    hashed_password = hash_password(password)
    new_user = {"username": username, "email": email, "password": hashed_password}
    add_record("users", new_user)

def authenticate_user(email, password):
    users_df = read_parquet("users")
    hashed_password = hash_password(password)
    user = users_df[(users_df["email"] == email) & (users_df["password"] == hashed_password)]
    if not user.empty:
        return True
    else:
        return False
