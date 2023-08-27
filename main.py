# Initialize an empty set to store tasks
todo_set = set()

# Function to add a task to the to-do list
def add_task(task):
    todo_set.add(task)
    print(f"Task {task} added to the to-do list.")

# Function to view tasks in the to-do list
def view_tasks():
    if not todo_set:
        print("The to-do list is empty.")
    else:
        print("Tasks in the to-do list:")
        for task in todo_set:
            print("•", task)

# Function to remove a task from the to-do list
def remove_task(task):
    if task in todo_set:
        todo_set.remove(task)
        print(f"Task {task} removed from the to-do list.")
    else:
        print(f"Task {task} not found in the to-do list.")

# Main program loop
while True:
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = int(input("Choose a number: "))

    if choice == 1:
        task_name = input("Task name: ")
        add_task(task_name)  # Call the add_task function
        print("Task added successfully!")

    elif choice == 2:
        view_tasks()  # Call the view_tasks function

    elif choice == 3:
        task_name = input("Task name: ")
        remove_task(task_name)  # Call the remove_task function

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")