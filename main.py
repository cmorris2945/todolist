

num = 0
while True:
    user_action = input("Welcome to the task todo list program. Just type what you want to do: add, show, edit,"
                        "completed, or exit...")
    user_action = user_action.strip()


    if 'add' in user_action:
        todo = user_action[4:]

        with open('file/subfiles/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('file/subfiles/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:

        with open('file/subfiles/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    elif 'edit' in user_action:
        number = int(input("Enter the number in the todo list to edit..."))
        number = number -1

        with open('file/subfiles/todos.txt', 'r') as file:
            todos = file.readlines()

        print("Here are the exitsting todos, Mac...", todos)

        new_todo = input("Enter the new todo...")
        todos[number] = new_todo + '\n'

        print("Here is how it will be done now....", todos)

    elif 'completed' in user_action:
        number = int(input("Number of the todo to complete: "))

        with open('file/subfiles/todos.txt', 'r') as file:
            todos = file.readlines()
        index = number -1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('file/subfiles/todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)

    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid. Please enter a valid command....")
print("get lost Jack!")
