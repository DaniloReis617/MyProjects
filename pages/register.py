import streamlit as st
import re
from utils.auth import register_user

def show():
    st.title("Registro")

    username = st.text_input("Nome de usuário")
    email = st.text_input("Email")
    password = st.text_input("Senha", type="password")
    confirm_password = st.text_input("Confirme a senha", type="password")

    if st.button("Registrar"):
        if not username or not email or not password or not confirm_password:
            st.error("Por favor, preencha todos os campos.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            st.error("Por favor, insira um email válido.")
        elif password != confirm_password:
            st.error("As senhas não coincidem.")
        else:
            try:
                register_user(username, email, password)
                st.success("Registro realizado com sucesso!")
            except ValueError as e:
                st.error(str(e))

if __name__ == "__main__":
    show()
