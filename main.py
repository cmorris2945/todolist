

num = 0
while True:
    user_action = input("Welcome to the task todo list program. Just type what you want to do: add, show, edit,"
                        "completed, or exit...")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") +"\n"
            file = open('file/subfiles/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('file/subfiles/todos.txt', 'w')
            file.writelines((todos))
        case 'show':
            file = open('file/subfiles/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Enter the number in the todo list to edit..."))
            number = number -1
            new_todo = input("Enter the new todo...")
            todos[number] = new_todo
        case 'completed':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number-1)


        case 'exit':
            break
