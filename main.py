# task-manager
# A simple command-line to-do list application written in Python.

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