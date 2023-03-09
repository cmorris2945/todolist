def get_todos():
    with open('file/subfiles/todos.txt', 'r') as file:
        todos = file.readlines()
    return todos

while True:
        user_action = input("Welcome to the task todo list program. Just type what you want to do: add, show, edit,"
                            "completed, or exit...")
        user_action = user_action.strip()


        if user_action.startswith("add"):
            todos = user_action[4:]

            todos = get_todos()

            todos.append(str(todos) + '\n')

            with open('file/subfiles/todos.txt', 'w') as file:
                file.writelines(todos)

        elif user_action.startswith("show"):

            todos = get_todos()

            todos.append(str(todos) + '\n')

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)
        elif user_action.startswith("edit"):
            try:
                number =int(user_action[5:])
                print(number)
                number = number -1

                todos = get_todos()

                new_todo = input("Enter the new todo...")
                todos[number] = new_todo + '\n'

                with open('todos.txt', 'w') as file:
                    file.writelines(todos)
            except ValueError:
                print("Your command is not valid")
                continue

        elif user_action.startswith("completed"):
            try:
                number = int(user_action[9:])

                todos = get_todos()
                index = number -1
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
print("get lost Jack!")
