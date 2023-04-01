def get_todos():
    with open('file/subfiles/todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

while True:
    user_action = input("Welcome to the task todo list program. Just type what you want to do: add, show, edit, completed, or exit...")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        new_todo = input("Enter the new todo...")
        todos = get_todos()
        todos.append(new_todo + '\n')
        with open('file/subfiles/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            new_todo = input("Enter the new todo...")
            todos[number] = new_todo + '\n'
            with open('file/subfiles/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("completed"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            with open('file/subfiles/todos.txt', 'w') as file:
                file.writelines(todos)
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
