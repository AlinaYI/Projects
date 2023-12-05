while True:
    user_action = input("Type add, show, edit,complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        #context manager
        with open('todos.txt','r') as file:
            todos = file.readlines()

        # append new todo into todos
        todos.append(todo + '\n')

        with open('todos.txt','w') as file:
            file.writelines(todos)
    elif user_action.startswith('show'):

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

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

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo:") + "\n"
            todos[number] = new_todo

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    # user finish a todo, need to remove one todo
    elif user_action.startswith('complete'):
        try:
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            number = int(user_action[9:])
            todo_to_remove = todos[number-1].strip('\n')
            todos.pop(number - 1)


            with open('todos.txt', 'w') as file:
                file.writelines(todos)

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
