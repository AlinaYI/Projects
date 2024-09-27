def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# this function is procedure, do not need to return anything
def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit,complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos("todos.txt")
        # append new todo into todos
        todos.append(todo + '\n')
        write_todos("todos.txt", todos)

    elif user_action.startswith('show'):

        todos = get_todos("todos.txt")

        for idx, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{idx + 1}-{item}"
            print(row)

    # user can edit the todo list
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            # index would be start from zero
            number = int(number) - 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter new todo:") + "\n"
            todos[number] = new_todo
            write_todos("todos.txt", todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    # user finish a todo, need to remove one todo
    elif user_action.startswith('complete'):
        try:
            todos = get_todos("todos.txt")

            number = int(user_action[9:])
            todo_to_remove = todos[number-1].strip('\n')
            todos.pop(number - 1)

            write_todos("todos.txt", todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid.")
print("Bye!")
