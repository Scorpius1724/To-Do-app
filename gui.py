import functions
import PySimpleGUI as sg
import time
import os


if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass


sg.theme("black")


clock = sg.Text('', key='clock')

label = sg.Text('Enter a To-Do item')

input_box = sg.InputText(tooltip='Enter To-Do', key='todo')
add_button = sg.Button('Add', tooltip='Add a To-Do Item')

list_box = sg.Listbox(values=functions.get_todos(), key='selected_todo', enable_events=True, size= [45, 10])
edit_button = sg.Button('Edit', tooltip='Edit a selected To-Do Item')
complete_button = sg.Button('Complete', tooltip='Remove the selected To-Do Item from the list')

exit_button = sg.Button('Exit')


window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                           font=('Helvetica', 20))


while True:
    event, values = window.read(timeout=100)
    window['clock'].update(value=time.strftime('DATE - %dth %b, %Y | TIME - %H:%M:%S'))


    match event:

        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['selected_todo'].update(values=todos)

        case 'Edit':
            try:
                todo_to_edit = values['selected_todo'][0]
                new_todo = values['todo'].strip('\n') + ('\n')
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['selected_todo'].update(values=todos)
            except IndexError:
                sg.popup("Select an item first", font=('Helvetica', 20))

        case 'Complete':
            try:
                todo_to_complete = values['selected_todo'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)

                window['selected_todo'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Select an item first", font=('Helvetica', 20))

        case 'selected_todo':
            window['todo'].update(value=values['selected_todo'][0])

        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

window.close()