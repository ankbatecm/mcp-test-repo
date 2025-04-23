from utils import load_tasks, save_tasks

def main():
    tasks = load_tasks()
    print("To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    new_task = input("Add a new task: ")
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task saved!")

if __name__ == "__main__":
    main()
