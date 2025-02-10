import os
import json
import dc
def load_tasks():
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as f:
            json.dump([], f)
    tasks = json.load(open('tasks.json'))
    return tasks

def add_task():
    tasks = load_tasks()
    task = (f"{input("Enter a task: ")} ")

    if task in tasks:
        print(f'Task {task} already exists!')
        return
    else:
        tasks.append(task)
        with open('tasks.json', 'w') as f:
            json.dump(tasks, f)
        print(f'Task {task} added successfully!')

def remove_task():
    tasks = load_tasks()
    if not tasks:
        print("There is nothing to do!")
        return
    else:
        print("List of tasks:")
        list_tasks()
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            with open('tasks.json', 'w') as f:
                json.dump(tasks, f)
            print(f'Task {task} removed successfully!')
        else:
            print(f'Task {task} not found!')

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("There is nothing to do!")
        return
    else:
        print("List of tasks:")
        print('-------------------')
        for task in tasks:
            print(task)
            print('-------------------')

def main():
    while True:
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                add_task()
            case "2":
                remove_task()
            case "3":
                list_tasks()
            case "4":
                break
            case _:
                print("Invalid choice")

if __name__ == '__main__':
    main()