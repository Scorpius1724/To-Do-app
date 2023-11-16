import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\ns'
    todos.append(todo)
    functions.write_todos(todos)

st.title("To-Do App")
st.subheader("This is my To-Do App")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)


st.text_input(label="", placeholder="Add new to-do...", on_change=add_todo, key='new_todo')

st.session_state