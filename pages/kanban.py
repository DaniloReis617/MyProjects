import streamlit as st
from utils.db import read_parquet

def show():
    st.title("Kanban")
    
    tasks_df = read_parquet("tasks")
    
    status_options = tasks_df["status"].unique()
    for status in status_options:
        st.subheader(status)
        tasks = tasks_df[tasks_df["status"] == status]
        for _, task in tasks.iterrows():
            st.write(f"**{task['task_name']}** - {task['assigned_to']} (Due: {task['due_date']})")

if __name__ == "__main__":
    show()
