header = """
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
                            
"""
print(header)
todos = []
todos_completed = []
while True:
    print("*" * 50)
    print("Enter a command. Type 'h' for help:")
    todo_num = 1
    todos_idx = []
    for todo in todos:
        print(f"{todo_num}){todo}")
        todos_idx.append(todo_num)
        todo_num += 1
        todos_idx = [str(idx) for idx in todos_idx]
    command = input("> ")
    if command == "h":
        print("TODO LIST HELP")
        print("Type 'q' to quit.")
        print("To add a todo to the list, type it and hit enter.")
        print("To complete a todo enter its number.")
    elif command == "q":
        if len(todos_completed) == 0:
            print()
        else:
            print(f"Today you completed {len(todos_completed)} todos:")
            for todo in todos_completed:
                print(f"* {todo}")
        break
    elif command.isnumeric() and command not in todos_idx:
        print("That is an incorrect index. Please use a number that is present on the list.")
    else:
        if command not in todos_idx:
            todos.append(command)
        elif command in todos_idx:
            command = int(command)
            removed_todo = todos.pop(command - 1)
            todos_completed.append(removed_todo)
        
        


