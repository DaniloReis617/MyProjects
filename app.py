import streamlit as st
import importlib.util
from utils.db import create_parquet_files, verify_parquet_files

# --- PAGE SETUP ---
PAGES = {
    "Login": {"module": "pages.login", "title": "Login", "icon": "🔑"},
    "Register": {"module": "pages.register", "title": "Register", "icon": "📝"},
    "Dashboard": {"module": "pages.dashboard", "title": "Dashboard", "icon": "📊"},
    "Kanban": {"module": "pages.kanban", "title": "Kanban", "icon": "📋"},
    "Table": {"module": "pages.table", "title": "Table", "icon": "📅"},
    "Create": {"module": "pages.create", "title": "Create", "icon": "➕"},
    "Edit": {"module": "pages.edit", "title": "Edit", "icon": "✏️"},
    "Delete": {"module": "pages.delete", "title": "Delete", "icon": "🗑️"},
}

# --- NAVIGATION SETUP [WITH SECTIONS] ---
SECTIONS = {
    "Authentication": ["Login", "Register"],
    "Management": ["Dashboard", "Kanban", "Table", "Create", "Edit", "Delete"],
}

# --- SHARED ON ALL PAGES ---
st.set_page_config(page_title="Project Management App", page_icon="📈", layout="wide")
st.sidebar.image("assets/logo.ico", use_column_width=True)

def load_page(module_name):
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        st.error(f"Não foi possível encontrar o módulo {module_name}")
        return None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    # Verificar e criar arquivos Parquet necessários
    create_parquet_files()
    verify_parquet_files()
    
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user_email = ""
        st.session_state.current_page = "Login"

    if st.session_state.logged_in:
        st.sidebar.title(f"Bem-vindo, {st.session_state.user_email}")
        for section, pages in SECTIONS.items():
            st.sidebar.subheader(section)
            for page in pages:
                if st.sidebar.button(PAGES[page]["title"], key=page):
                    st.session_state.current_page = page
    else:
        st.sidebar.title("Por favor, faça login")

    page_module = load_page(PAGES[st.session_state.current_page]["module"])
    if page_module and hasattr(page_module, 'show'):
        page_module.show()
    else:
        st.error(f"A página {st.session_state.current_page} não possui uma função 'show'.")

if __name__ == "__main__":
    main()
