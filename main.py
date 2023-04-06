def get_todos(filepath):
    with open(filepath) as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Welcome to the task todo list program. Just type what you want to do: add, show, edit, completed, or exit...")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        #new_todo = input("Enter the new todo...")
        todos = get_todos('file/subfiles/todos.txt')
        todos.append(todo + '\n')

        write_todos("file/subfiles/todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos('file/subfiles/todos.txt')
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number -1
            todos = get_todos('file/subfiles/todos.txt')
            new_todo = input("Enter the new todo...")
            todos[number] = new_todo + '\n'
            write_todos('file/subfiles/todos.txt', todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("completed"):
        try:
            number = int(user_action[9:])
            todos = get_todos('file/subfiles/todos.txt')
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos('file/subfiles/todos.txt', todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number chump! Try again...")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid. Please enter a valid command....")

print("Goodbye!")
