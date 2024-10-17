# app.py
import streamlit as st
from database.db_operations import setup_database
from pages import home, dashboard, projects, add_project

class GestaoProjetosApp:
    def __init__(self):
        setup_database()
        st.set_page_config(page_title="Gestão de Projetos", layout="wide")
        self.pages = {
            "Home": home.show,
            "Dashboard": dashboard.show,
            "Projetos": projects.show,
            "Adicionar Projeto": add_project.show
        }

    def run(self):
        st.sidebar.title("Menu de Navegação")
        selection = st.sidebar.radio("Ir para", list(self.pages.keys()))
        page = self.pages[selection]
        page()

if __name__ == "__main__":
    app = GestaoProjetosApp()
    app.run()