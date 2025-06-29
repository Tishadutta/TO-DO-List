tasks = []  # List to store all tasks

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task_name = input("Enter the task: ")
        task = {"task": task_name, "done": False}
        tasks.append(task)
        print(f"Task '{task_name}' added.")

    elif choice == "2":
        if not tasks:
            print("No tasks to show.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "✅" if task["done"] else "❌"
                print(f"{i}. {task['task']} [{status}]")

    elif choice == "3":
        if not tasks:
            print("No tasks to mark as done.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✅" if task["done"] else "❌"
                print(f"{i}. {task['task']} [{status}]")

            task_num = int(input("Enter task number to mark as done: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["done"] = True
                print(f"Task {task_num} marked as done.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']}")

            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Deleted task: {removed_task['task']}")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
