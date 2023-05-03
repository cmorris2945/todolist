import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(size=20,image_source="add.png", mouseover_colors="Red",
                       tooltip="This is to add something to the list", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button(size=20, image_source="complete.png",mouseover_colors="LightBlue2",
                        tooltip="This button is to edit something in the list", key="Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button('Exit')

window = sg.Window("My To-Do App",
                   layout=[[clock],
                         [label],
                          [input_box, add_button],
                          [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    if event == sg.WINDOW_CLOSED:
        break
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:

                todo_to_edit = values['todos'][0]
                new_todo = values['todo']  # Update this line to get the value from the input_box

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"  # Add a newline character to the new_todo before updating
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first...", font=('Helvetica', 20))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first...", font=('Helvetica', 20))

        case  "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WINDOW_CLOSED:
            break
print("Bye ")

window.close()


