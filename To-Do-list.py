
tasks = []
completed_tasks = []

try:
    with open("tasks.txt", "r") as file:
        for line in file:
            task, status = line.strip().split("|")
            if status == "completed":
                completed_tasks.append(task)
            else:
                tasks.append(task)
except FileNotFoundError:
    pass


while True:
    print("\n--- TO DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")
        if not tasks and not completed_tasks:
            print("No tasks available.")

        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

        for i in range(len(completed_tasks)):
            print(i + 1, ".", completed_tasks[i], "(Completed)")

    elif choice == "3":
        if not tasks:
            print("No tasks to complete.")
            continue

        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

        num = int(input("Enter task number to mark completed: "))

        if 1 <= num <= len(tasks):
            completed_tasks.append(tasks[num - 1])
            tasks.pop(num - 1)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
            continue

        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

        num = int(input("Enter task number to delete: "))

        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted!")
        else:
            print("Invalid task number.")

    elif choice == "5":
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "|pending\n")
            for task in completed_tasks:
                file.write(task + "|completed\n")

        print("Tasks saved. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
