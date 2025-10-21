# File to store tasks
TASK_FILE = "tasks.txt"

# Load tasks from file (if exists)
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found.")
    else:
        print("\n📝 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Add a new task
def add_task(tasks):
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added successfully!")
    else:
        print("⚠️ Task cannot be empty!")

# Remove a task by its number
def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter the task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"🗑️ Task '{removed}' removed.")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n========= TO-DO LIST =========")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        print("==============================")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Exiting... Your tasks are saved.")
            break
        else:
            print("⚠️ Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()
