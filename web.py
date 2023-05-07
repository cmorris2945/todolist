import streamlit as st
from functions import *
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    write_todos(todos)

    #st.experimental_rerun()

todos = get_todos()


st.title("My Todo Application")
st.subheader("This is my todo application")
st.write("(Hopefully this application with increase your productivity...)")


for index, todo in enumerate(todos):
    st.checkbox(todo, key=f"todo_{index}")


st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')

print("Hello")
