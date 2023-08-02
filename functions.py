def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file:
        todos_temp = file.readlines()
    return todos_temp


def set_todos(data, filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(data)


if __name__ == "__main__":
    print('HI')
