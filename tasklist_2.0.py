class Task:
    def __init__(self, description, tag=None):
        self.description = description
        self.tag = tag

def display_tasks(task_list):
    print("TASKLIST")
    print("-------------------")
    
    for index, task in enumerate(task_list, start=1): 
        tag_info = f"({task.tag})" if task.tag else ""
        print(f"{index}. {task.description} {tag_info}")

    print("-------------------")

def mark_task_as_done(task_list):
    display_tasks(task_list)
    
    try:
        task_number = int(input("Enter the task number to mark as done: "))
        comment = input("Enter a comment (e.g., 'done'): ")

        if 1 <= task_number <= len(task_list):
            task_list[task_number - 1].tag = comment
            print(f"Task {task_number} marked as {comment}.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Example usage:
tasks = [Task("Task 1"), Task("Task 2"), Task("Task 3")]

while True:
    print("MENU OF TASKLIST")
    print("-------------------")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Remove Tasks")
    print("4. Mark Tasks")
    print("5. Quit")
    print("-------------------")

    choice = input("Select: ")

    if choice == "1":
        display_tasks(tasks)
    elif choice == "2":
        task_description = input("Enter the task description: ")
        tasks.append(Task(task_description))
        print("Task added.")
    elif choice == "3":
        display_tasks(tasks)
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                del tasks[task_number - 1]
                print(f"Task {task_number} removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == "4":
        mark_task_as_done(tasks)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid selection.")