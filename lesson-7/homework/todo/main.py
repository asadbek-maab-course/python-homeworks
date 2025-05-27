from task import Task
from storage.csv_storage import CSVStorage
from storage.json_storage import JSONStorage

def choose_storage():
    choice = input("Choose storage format (1 = CSV, 2 = JSON): ")
    if choice == '1':
        return CSVStorage('tasks.csv')
    else:
        return JSONStorage('tasks.json')

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

def main():
    storage = choose_storage()
    tasks = storage.load_tasks()

    while True:
        print("\nWelcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            task = Task(
                task_id=input("Enter Task ID: "),
                title=input("Enter Title: "),
                description=input("Enter Description: "),
                due_date=input("Enter Due Date (YYYY-MM-DD): "),
                status=input("Enter Status (Pending/In Progress/Completed): ")
            )
            tasks.append(task)
            print("Task added successfully!")

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            task_id = input("Enter Task ID to update: ")
            for task in tasks:
                if task.task_id == task_id:
                    task.title = input("New Title: ")
                    task.description = input("New Description: ")
                    task.due_date = input("New Due Date: ")
                    task.status = input("New Status: ")
                    print("Task updated.")
                    break
            else:
                print("Task not found.")

        elif choice == '4':
            task_id = input("Enter Task ID to delete: ")
            tasks = [t for t in tasks if t.task_id != task_id]
            print("Task deleted if it existed.")

        elif choice == '5':
            status = input("Enter status to filter by: ")
            filtered = [t for t in tasks if t.status.lower() == status.lower()]
            display_tasks(filtered)

        elif choice == '6':
            storage.save_tasks(tasks)
            print("Tasks saved.")

        elif choice == '7':
            tasks = storage.load_tasks()
            print("Tasks loaded.")

        elif choice == '8':
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
