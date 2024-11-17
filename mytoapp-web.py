import streamlit as st
import functions
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt','w') as file:
        pass

todos=[]
def add_todo():
    todo=st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)




todos=functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

"""Below code is for removing item from ui which is checked"""
for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        """Below will delete from session state dictionary"""
        del st.session_state[todo]
        st.experimental_rerun()



st.text_input(label = "Enter a todo: ",placeholder="Add new todo...",
              on_change=add_todo,key='new_todo')

st.session_state