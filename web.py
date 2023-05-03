import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo Application")
st.subheader("This is my todo application")
st.write("(Hopefully this application with increase your productivity...)")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo...")