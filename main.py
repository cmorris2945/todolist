

todos = []
num = 0
while True:
    user_action = input("Welcome to the task todo list program. Just type what you want to do: add, show. edit,"
                        " or exit...")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Enter the number in the todo list to edit..."))
            number = number -1
            new_todo = input("Enter the new todo...")
            todos[number] = new_todo

        case 'exit':
            break


