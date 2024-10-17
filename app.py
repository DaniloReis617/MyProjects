import streamlit as st
from auth import login
from pages import home, projetos_crud
from dashboard import dashboard
from database import init_parquet

init_parquet()

# Autenticação
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    login()
else:
    # Barra de navegação lateral
    st.sidebar.title("Menu")
    menu = ["Home", "Dashboard", "Projetos (CRUD)", "Logout"]
    choice = st.sidebar.selectbox("Navegação", menu)

    if choice == "Home":
        home.home()
    elif choice == "Dashboard":
        dashboard.dashboard()
    elif choice == "Projetos (CRUD)":
        projetos_crud.crud_projects()
    elif choice == "Logout":
        st.session_state['logged_in'] = False
        st.rerun()  # Atualiza a página
