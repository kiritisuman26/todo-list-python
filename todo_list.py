tasks = []
print("Welcome to the To-Do List App!")
while True:
    print("\nPlease choose an option:")
    print("1. View a task")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        if not tasks:
            print("Your to-do list is empty.")
        else:       
            print("Your to-do list:")
            print("------YOUR TASKS-------")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif choice == '2':
        task = input("Enter the task you want to add: ")
        tasks.append(task)
        print(f"Task '{task}' added to the list.")
    elif choice == '3':
        if not tasks:
            print("Your to-do list is empty.")
        else:
            to_remove = input("Enter the task you want to remove: ")
            if to_remove in tasks:
                tasks.remove(to_remove)
                print(f"Task '{to_remove}' removed from the list.")
            else:
                print(f"Task '{to_remove}' not found in the list.")
    elif choice == '4':
        print("Exiting the To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.") 

