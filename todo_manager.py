import json
import os

FILE_NAME = "todo_list.json"


# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\n========== YOUR TO-DO LIST ==========")

    for i, task in enumerate(tasks, start=1):
        status = "✓ Completed" if task["completed"] else "✗ Pending"
        print(f"{i}. {task['title']} - {status}")

    print("=====================================")


# Add a new task
def add_task(tasks):
    title = input("\nEnter the task: ").strip()

    if title == "":
        print("Task cannot be empty.")
        return

    tasks.append({
        "title": title,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added successfully!")


# Mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("\nEnter the task number to mark as completed: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Delete a task
def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("\nEnter the task number to delete: "))

        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed_task['title']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Search for a task
def search_tasks(tasks):
    keyword = input("\nEnter a keyword to search: ").strip().lower()

    results = [
        task for task in tasks
        if keyword in task["title"].lower()
    ]

    if not results:
        print("No matching tasks found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    for i, task in enumerate(results, start=1):
        status = "✓ Completed" if task["completed"] else "✗ Pending"
        print(f"{i}. {task['title']} - {status}")

    print("====================================")


# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n")
        print("╔══════════════════════════════╗")
        print("║       TO-DO LIST MANAGER     ║")
        print("╠══════════════════════════════╣")
        print("║ 1. Add Task                  ║")
        print("║ 2. View Tasks                ║")
        print("║ 3. Complete Task             ║")
        print("║ 4. Delete Task               ║")
        print("║ 5. Search Tasks              ║")
        print("║ 6. Exit                      ║")
        print("╚══════════════════════════════╝")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            search_tasks(tasks)

        elif choice == "6":
            print("\nTasks saved successfully.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()
