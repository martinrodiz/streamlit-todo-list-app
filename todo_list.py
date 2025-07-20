# Importaciones
import streamlit as st

from quote import generate_quote
from task import Task

# Información persistente entre sesiones

if "task_list" not in st.session_state:
    st.session_state.task_list = []
task_list = st.session_state.task_list

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

if "quote" not in st.session_state:
    api_key = st.secrets["quotes_api"]["api_key"]
    st.session_state.quote = generate_quote(api_key)


# Funciones
def add_task(task_name: str):
    task_list.append(Task(task_name))


def mark_done(task: Task):
    task.is_done = True


def mark_not_done(task: Task):
    task.is_done = False


def delete_task(idx: int):
    del task_list[idx]
    st.rerun()


# Frontend
with st.sidebar:
    task = st.text_input("Escribir tarea")
    if st.button("Añadir tarea", type="primary"):
        add_task(task)

st.header("Lista de tareas", divider="gray")

# st.subheader("Tu dosis diaria de inspiración:")
st.info(st.session_state.quote)

total_task = len(task_list)
completed_task = sum(1 for task in task_list if task.is_done)
metric_display = (
    f"{completed_task}/{total_task}"
    f"{'tareas completadas' if total_task >= 2 else 'tarea completada'}"
)
st.metric("", metric_display, delta=None)
if completed_task == total_task and total_task != 0:
    st.success("!Terminaste las tareas!", icon="✔️")

for idx, my_task in enumerate(task_list):
    task_col, delete_col = st.columns([0.8, 0.2])
    label = f"~~{my_task.name}~~" if my_task.is_done else my_task.name
    checked = task_col.checkbox(label, my_task.is_done, key=f"task_{idx}")
    if checked and not my_task.is_done:
        mark_done(my_task)
        st.rerun()
    elif not checked and my_task.is_done:
        mark_not_done(my_task)
        st.rerun()
    if delete_col.button("Eliminar", key=f"eliminar_{idx}"):
        delete_task(idx)
