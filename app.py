import sys
import json


TASKS_FILE = "tasks.json"

def add_task(task_text):
    tasks = load_tasks()
    tasks.append(task_text)
    save_tasks(tasks)

    print(f"task added: {task_text}")


def load_tasks():
    with open(TASKS_FILE, "r") as file:
        tasks = json.load(file)
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)



def list_tasks():
    tasks= load_tasks()

    if len(tasks) == 0:
        print("no tasks found")
        return

    print("tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def search_tasks(search_text):
    tasks = load_tasks()

    found_match = False

    for index, task in enumerate(tasks, start=1):
        if search_text.lower() in task.lower():
            print(f"{index}. {task}")
            found_match = True

    if not found_match:
        print("no matching tasks found")

def delete_task(task_number):
    tasks = load_tasks()

    if task_number < 1 or task_number > len(tasks):
        print("task number not found")
        return
    
    task_index = task_number - 1
    deleted_task = tasks.pop(task_index)
    save_tasks(tasks)

    print(f"deleted task: {deleted_task}")


def complete_task(task_number):
    tasks = load_tasks()

    if task_number < 1 or task_number > len(tasks):
        print("task number not found")
        return
    
    task_index = task_number - 1
    tasks[task_index] = "[x] " + tasks[task_index]
    save_tasks(tasks)

    print(f"completed task: {tasks[task_index]}")

def main():
    if len(sys.argv) < 2:
        print("please provide a command")
        return
    
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("please provide a task to add")
            return
        
        task_text = sys.argv[2]
        add_task(task_text)
                 
    elif command == "list":
        list_tasks()

    elif command == "delete":
        if len(sys.argv) < 3:
            print("please provide a task number to delete")
            return
    
        try:
            task_number = int(sys.argv[2])
        except ValueError:
            print("invalid task number")
            return
        
        delete_task(task_number)

    elif command == "search":
        if len(sys.argv) < 3:
            print("please provide a search text")
            return
        
        search_text = sys.argv[2]
        search_tasks(search_text)


    elif command == "complete":
        if len(sys.argv) < 3:
            print("please provide a task number to complete")
            return
    
        try:
            task_number = int(sys.argv[2])
        except ValueError:
            print("invalid task number")
            return
        
        complete_task(task_number)


    else:
        print("unknown command")

    
main()