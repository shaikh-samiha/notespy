import os

FILENAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\n🔹 No tasks available.")
    else:
        print("\n📝 To-Do List:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("✅ Task added!")

def mark_done(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to mark done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index] = f"{tasks[index]} ✅"
        print("✔️ Task marked as done!")
    else:
        print("❌ Invalid task number!")

def delete_task(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("🗑️ Task deleted!")
    else:
        print("❌ Invalid task number!")

def main():
    tasks = load_tasks()
    while True:
        print("\n===== To-Do Menu =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("📁 Tasks saved. Goodbye!")
            break
        else:
            print("⚠️ Invalid option! Please try again.")

if __name__ == "__main__":
    main()
