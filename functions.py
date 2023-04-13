def get_todos(filepath='file/subfiles/todos.txt'):
    """Reads a text file and
    returns the list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath="file/subfiles/todos.txt"):
    """ Writes the to-do items int eh list in the text files"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
