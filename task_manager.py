
import os

TASKS_FILE = 'tasks.txt'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return [task.strip() for task in file.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(task, tasks):
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")


def remove_task(task_number, tasks):
    try:
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{removed}' removed.")
    except IndexError:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTask Manager")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            task = input("Enter a task: ")
            add_task(task, tasks)
        elif choice == '3':
            show_tasks(tasks)
            task_number = int(input("Enter task number to remove: "))
            remove_task(task_number, tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
