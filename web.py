import streamlit as st
import functions

todos = functions.get_todos()

st.title("To-Do App")
st.subheader("This is my To-Do App")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)


st.text_input("", placeholder="Add new to-do...")
