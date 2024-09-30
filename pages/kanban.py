import streamlit as st
from streamlit_elements import elements, dashboard, mui

st.set_page_config(layout="wide")

if 'tasks' not in st.session_state:
    st.session_state.tasks = [
        {"id": 1, "title": "Tarefa 1", "status": "To Do"},
        {"id": 2, "title": "Tarefa 2", "status": "In Progress"},
        {"id": 3, "title": "Tarefa 3", "status": "Done"}
    ]

def render_kanban():
    with elements("kanban"):
        with dashboard.Grid():
            for task in st.session_state.tasks:
                with mui.Card(key=task["id"]):
                    mui.CardHeader(title=task["title"])
                    mui.CardContent(task["status"])

if __name__ == "__main__":
    st.title("Quadro Kanban")
    render_kanban()
