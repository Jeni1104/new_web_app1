def get_todos(filepath = "File2.txt" ):
    """This function read file and return the data of file"""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

#print(help(get_todos))
def write_todos(todos_arg, filepath = "File2.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)