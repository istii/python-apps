import functions
import PySimpleGUI as sg
import time

sg.theme('DarkBlue')
clock = sg.T('', key='clock')
label = sg.Text("Type in a To-Do:")
input_box = sg.InputText(tooltip="Enter Todo", key='todo')
add_button = sg.Button("Add")
edit_button = sg.B("Edit")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
complete_button = sg.B('Complete')
exit_button = sg.B('Exit')
window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Times New Roman', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
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
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an Item first", font=("Times new roman", 20))
        case 'Complete':
            try:
                todos_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todos_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an Item first", font=("Times new roman", 20))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
        case sg.WINDOW_CLOSED:
            break
window.close()
