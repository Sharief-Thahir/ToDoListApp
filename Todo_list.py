tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    if tasks:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")

def main():
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            task = input("Enter a task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
