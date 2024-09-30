import streamlit as st
from pages import login, register, dashboard, kanban, table, create, edit, delete

PAGES = {
    "Login": login,
    "Register": register,
    "Dashboard": dashboard,
    "Kanban": kanban,
    "Table": table,
    "Create": create,
    "Edit": edit,
    "Delete": delete
}

def main():
    st.sidebar.title("Navegação")
    selection = st.sidebar.radio("Ir para", list(PAGES.keys()))
    page = PAGES[selection]
    page.show()

if __name__ == "__main__":
    main()
