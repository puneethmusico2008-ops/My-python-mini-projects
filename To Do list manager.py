'''
This script checks about the list of tasks to be done. It allows the user to add, view, and delete tasks from a to-do list.
'''

print("=======> To-Do List Manager <=======")

tasks = []

while True:
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Mark a task as completed")
    print("5. Exit")

    choice = input("ENTER YOUR CHOICE (1-5): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == '2':
        if not tasks:
            print("No tasks available.")
        else:
            print("Tasks in the to-do list:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == '3':
        if not tasks:
            print("No tasks available to delete.")
        else:
            try:
                task_number = int(input("Enter the task number to delete: "))
                if 1 <= task_number <= len(tasks):
                    deleted_task = tasks.pop(task_number - 1)
                    print(f"Task '{deleted_task}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':
        if not tasks:
            print("No tasks available to mark as completed.")
        else:
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                if 1 <= task_number <= len(tasks):
                    completed_task = tasks[task_number - 1]
                    print(f"Task '{completed_task}' marked as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '5':
        print("Exiting the To-Do List Manager.")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 5.")

