import streamlit as st

# Usuários predefinidos para o login
usuarios = {"admin": "admin123", "user": "user123"}

def login():
    st.title("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    login_button = st.button("Entrar")

    if login_button:
        if username in usuarios and usuarios[username] == password:
            st.session_state['logged_in'] = True
            st.success(f"Bem-vindo, {username}!")
        else:
            st.error("Usuário ou senha inválidos.")
