# Simple To-Do List App
tasks = []
def view_tasks():
    if len(tasks) == 0:
        print("No tasks in the list!")
    else:
        print("Your Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def delete_task():
    view_tasks()
    if len(tasks) > 0:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted successfully!")
        else:
            print("Invalid task number!")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")