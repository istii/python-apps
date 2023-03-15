import os

def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def add_todo(todos, todo):
    todos.append(todo + "\n")
    write_todos(filepath, todos)

def show_todo(todos):
    for index, item in enumerate(todos):
        item = item.capitalize()
        item = item.strip('\n')
        index += 1
        row = f"{index}. {item}"
        print(row)

def edit_todo(todos, number, new_todo):
    number -= 1
    todos[number] = new_todo + "\n"
    write_todos(filepath, todos)

def complete_todo(todos, number):
    index = number - 1
    todo_to_remove = todos[index].strip('\n')
    todos.pop(index)
    write_todos(filepath, todos)
    message = f"Todo {todo_to_remove} was removed from the list"
    print(message)

def main():
    filepath = '../todos.txt'
    actions = {
        "add": add_todo,
        "show": show_todo,
        "edit": edit_todo,
        "complete": complete_todo,
        "exit": exit
    }

    while True:
        user_action = input("Type add, show, edit, complete or exit: ")
        user_action = user_action.strip()
        try:
            command, *args = user_action.split()
            todos = get_todos(filepath)
            actions[command](todos, *args)
        except KeyError:
            print("Invalid command")
        except Exception as e:
            print("An error occured: ", e)
    print("Bye!")

if __name__ == "__main__":
    main()
