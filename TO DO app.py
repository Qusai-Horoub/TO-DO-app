import sys

tasks= []

class Task:
    def __init__(self, name, description, category, priority, status):
        self.name = name
        self.description = description
        self.category = category
        self.priority = priority
        self.status = "TO DO"

def add_task(name, description, category, priority, status):
    task = Task(name, description, category, priority, status)
    tasks.append(task)
    print("The Task added ")

def edit_task(task_num, new_name, new_description, new_category, new_priority):
    index = int(task_num)-1
    if 0 <= index < len(tasks):
        task = tasks[index]
        task.name = new_name
        task.description = new_description
        task.category = new_category
        task.priority = new_priority
        print("The task edited ")
    else:
        print("Invalid task number ")

def change_status(task_num, new_status):
     index = int(task_num)-1
     if 0 <= index < len(tasks):
        task = tasks[index]
        task.status = new_status
        print("The task status changed ")
     else:
        print("Invalid task number ")

def delete_task(task_num):
     index = int(task_num)-1
     if 0 <= index < len(tasks):
         tasks.pop(index)
         print("The task deleted")
         
def exit():
    sys.exit()

while True: 
    print("\nTO DO list app: ")
    print("1. Add task ")
    print("2. Edit task ")
    print("3. Change task status ")
    print("4. Delete task ")
    print("5. Print tasks with 'done' status ")
    print("6. Print tasks with 'canceled' status ")
    print("7. Print all tasks ")
    print("8. Print tasks by category ")
    print("9. Sort and print tasks ")
    print("10. Exit ")

choice = input("Enter # your choice: ")

match int(choice):  
    case "1":
        name = input("Enter name of the task ")
        description = input("Enter description of the task ")
        category = input("Enter category of the task ")
        priority = input("Enter priority of the task ")
        add_task(name, description, category, priority)
    case "2":
        task_num = input("\nEnter # of task you want edit")
        new_name = input("Enter name of the task ")
        new_description = input("Enter description of the task ")
        new_category = input("Enter category of the task ")
        new_priority = input("Enter priority of the task ")
        edit_task(task_num, new_name, new_description, new_category, new_priority)
    case "3":
        task_num = input("\nEnter # of task you want change status ")
        new_status = input("Enter the new status ")
        change_status(task_num, new_status)
    case "4":
        task_num = input("\nEnter # of task you want delete it ")
        delete_task(task_num)
    case "5":
        print_done_status()
    case "6":
        print_canceled_status()
    case "7":
        print_tasks()
    case "8":
        print_task_by_category()
    case "9":
        print_sorted_tasks()
    case "10":
        exit()
    case _: 
        print("INVALID CHOICE.")
        print("\nPlease try again: ")