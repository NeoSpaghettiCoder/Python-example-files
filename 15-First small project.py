# Todo!
# 1-Add error check system
# 2-Change list to set or dictionary
# 3-Load choosen files by user
# 4-Mark tasks that have been made
# 5-Change files format
# 6-Change tasks for the categories
# 7-Automatic data save

user_choice = -1                                                        # Variable to select what operation user choice
tasks = []                                                              # List that saves tasks

def show_tasks():                                                       # Showing tasks in the list
    task_index = 0
    for task in tasks:
        print(task + " [" + str(task_index) + "]")
        task_index+=1

def add_task():                                                         # Adding task to the list
    task = input("Type what task is it: ")
    tasks.append(task)
    print("The task has been added")

def delete_task():                                                      # Deleting task from the list
    task_index = int(input("Select index to remove: "))

    if task_index < 0 or task_index > len(tasks)-1:
        print("Task doesn't exist")
        return
    tasks.pop(task_index)
    print("Your task has been deleted")

def save_tasks_to_file():                                               # Save tasks to the file 
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + '\n')

    file.close()

def load_tasks_from_file():                                             # Load tasks from the file
    try:
        file = open("tasks.txt")

        for line in file.readlines():
            tasks.append(line.strip())

        file.close()
    except FileNotFoundError:
        return

load_tasks_from_file()

while user_choice !=5:
    if(user_choice == 1):
        show_tasks()

    if user_choice == 2:
        add_task()

    if(user_choice == 3):
        delete_task()

    if(user_choice == 4):
        save_tasks_to_file()

    if(user_choice == 5):
        break

    print()
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Save changes into the file")
    print("5. Exit")

    user_choice = int(input("Select the number: "))
    print()