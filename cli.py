# from functions import get_todos, write_todos
import functions
import time


now = time.strftime("%dth %b, TIME- %H:%M:%S")
print("Today is", now)


while True:
    user_action = input("write add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        
        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            display_prompt = f"{index + 1}. {item}"
            print(display_prompt)

    elif user_action.startswith('edit'):

        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter the new Todo item: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):

        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            complete_message = f"The task {todo_to_remove} is completed and sucessfully removed from the list."
            print(complete_message)

        except IndexError:
            print("There is no item with the number you entered.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid command!")

print("Thank you for using our Todo list!!")
