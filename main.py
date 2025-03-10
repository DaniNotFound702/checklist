import os
import json
import save
import prepear

def prepere():
    with open("/home/daniel/.config/hypr/hyprland.conf", "a") as f:
        f.write("exec=/bin/python3 /home/daniel/.config/hypr/save.py")
def load_tasks():
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as f:
            json.dump({}, f)
    tasks = json.load(open('tasks.json'))
    if not isinstance(tasks, dict):
        tasks = {}
    return tasks

def add_task():
    tasks = load_tasks()
    task = input("Enter a task: ")
    state = "not done"

    if task in tasks:
        print(f'Task {task} already exists!')
        return
    else:
        tasks[task] = state

        with open('tasks.json', 'w') as f:
            json.dump(tasks, f)
        print(f'Task {task} added successfully!')

def remove_task():
    tasks = load_tasks()
    if not tasks:
        print("There is nothing to do!")
        return
    else:
        list_tasks()
        task = input("Enter task to remove: ")
        if task in tasks:
            del tasks[task]
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
        for task, state in tasks.items():
            print(f"{task}: {state}")
            print('-------------------')

def check_state():
    tasks = load_tasks()
    list_tasks()
    if not tasks:
        print("There is nothing to do!")
        return
    else:
        task = input("Enter task to check: ")
        if task in tasks:
            tasks[task] = "done"
            with open('tasks.json', 'w') as f:
                json.dump(tasks, f)
            print(f'Task {task} checked successfully!')
        else:
            print(f'Task {task} not found!')

def uncheck_state():
    tasks = load_tasks()
    list_tasks()
    if not tasks:
        print("There is nothing to do!")
        return
    task = input("Enter task to uncheck: ")
    if task in tasks:
        tasks[task] = "not done"
        with open('tasks.json', 'w') as f:
            json.dump(tasks, f)
        print(f'Task {task} unchecked successfully!')
    else:
        print(f'Task {task} not found!')

def main():
    while True:
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Check state")
        print("5. Uncheck state")
        print("6. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                add_task()
            case "2":
                remove_task()
            case "3":
                list_tasks()
            case "4":
                check_state()
            case "5":
                uncheck_state()
            case "6":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice")
prepear.main()
save.main()

if __name__ == '__main__':
    main()
