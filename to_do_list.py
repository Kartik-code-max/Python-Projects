def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")


def todo_list():
    tasks = []
    while True:
        print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a task: ")
            tasks.append(task)
            print("Task added.")
        elif choice == '2':
            display_tasks(tasks)
            task_num = int(input("Enter task number to remove: "))
            if 0 < task_num <= len(tasks):
                tasks.pop(task_num - 1)
                print("Task removed.")
            else:
                print("Invalid task number.")
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")


todo_list()
