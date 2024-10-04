import streamlit as st
import re
from utils.auth import authenticate_user

def show():
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Senha", type="password")

    if st.button("Login"):
        if not email or not password:
            st.error("Por favor, preencha todos os campos.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            st.error("Por favor, insira um email válido.")
        else:
            if authenticate_user(email, password):
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.session_state.current_page = "Dashboard"
                st.success("Login realizado com sucesso!")
                st.rerun()
            else:
                st.error("Email ou senha incorretos.")

if __name__ == "__main__":
    show()
