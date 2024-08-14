import sys

tasks = []

class Task:
    def __init__(self, name, description, category, priority):
        self.name = name
        self.description = description
        self.category = category
        self.priority = priority
        self.status = "TO DO"

    def __str__(self):
        return f"{self.name} - {self.description} - {self.category} - {self.priority} - {self.status}"

class ToDoList:
    @staticmethod
    def add_task(name, description, category, priority):
        task = Task(name, description, category, priority)
        tasks.append(task)
        print("Task added.")

    @staticmethod
    def edit_task(task_num, new_name, new_description, new_category, new_priority):
        index = int(task_num) - 1
        if 0 <= index < len(tasks):
            task = tasks[index]
            task.name = new_name
            task.description = new_description
            task.category = new_category
            task.priority = new_priority
            print("Task edited.")
        else:
            print("Invalid task number.")

    @staticmethod
    def move_task(task_num, new_status):
        index = int(task_num) - 1
        if 0 <= index < len(tasks):
            task = tasks[index]
            task.status = new_status
            print("Task status changed.")
        else:
            print("Invalid task number.")

    @staticmethod
    def delete_task(task_num):
        index = int(task_num) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task deleted.")
        else:
            print("Invalid task number.")

    @staticmethod
    def print_task(status=None, category=None):
        if status:
            filtered_tasks = [task for task in tasks if task.status == status]
        elif category:
            filtered_tasks = [task for task in tasks if task.category == category]
        else:
            filtered_tasks = tasks
        
        for index, task in enumerate(filtered_tasks):
            print(f"[{index + 1}] {task}")

    @staticmethod
    def sort_tasks(order):
        sorted_tasks = sorted(tasks, key=lambda x: x.name, reverse=(order.lower() == "descending"))
        for index, task in enumerate(sorted_tasks):
            print(f"[{index + 1}] {task}")

    @staticmethod
    def exit():
        sys.exit()

def main():
    while True: 
        print("\nTO DO list app:")
        print("1. Add task")
        print("2. Edit task")
        print("3. Change task status")
        print("4. Delete task")
        print("5. Print tasks with 'done' status")
        print("6. Print tasks with 'canceled' status")
        print("7. Print all tasks")
        print("8. Print tasks by category")
        print("9. Sort and print tasks")
        print("10. Exit")

        choice = input("Enter # your choice: ")

        try:
            choice = int(choice)
            match choice:
                case 1:
                    name = input("Enter name of the task: ")
                    description = input("Enter description of the task: ")
                    category = input("Enter category of the task: ")
                    priority = input("Enter priority of the task: ")
                    ToDoList.add_task(name, description, category, priority)
                case 2:
                    task_num = input("\nEnter # of task you want to edit: ")
                    new_name = input("Enter new name of the task: ")
                    new_description = input("Enter new description of the task: ")
                    new_category = input("Enter new category of the task: ")
                    new_priority = input("Enter new priority of the task: ")
                    ToDoList.edit_task(task_num, new_name, new_description, new_category, new_priority)
                case 3:
                    task_num = input("\nEnter # of task you want to change status: ")
                    new_status = input("Enter the new status: ")
                    ToDoList.move_task(task_num, new_status)
                case 4:
                    task_num = input("\nEnter # of task you want to delete: ")
                    ToDoList.delete_task(task_num)
                case 5:
                    ToDoList.print_task(status="done")
                case 6:
                    ToDoList.print_task(status="canceled")
                case 7:
                    ToDoList.print_task()
                case 8:
                    category = input("Enter the category of tasks you want to print: ")
                    ToDoList.print_task(category=category)
                case 9:
                    order = input("Enter the order in which you want to sort the task list ('ascending' or 'descending'): ")
                    ToDoList.sort_tasks(order)
                case 10:
                    ToDoList.exit()
                case _:
                    print("INVALID CHOICE. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
