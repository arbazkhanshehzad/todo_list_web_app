import streamlit as st
import functions


todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.set_todos(todos)
    print(todo)


st.title('My todo App <3')
st.subheader('This app is nice')
st.write('''This webapp is to store your
            to-do list and help you
            accomplish your goals in time''')

st.subheader("Here are you previous to-do's")
for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.set_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='', placeholder='Add new Todos...',
              on_change=add_todo, key='new_todo')