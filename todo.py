import csv
import os

class ToDo:
    def _init_(self, name, priority, status="Pending"):
        self.name = name
        self.priority = priority
        self.status = status

class ToDoList:
    def _init_(self, filename="tasks.csv"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        tasks = []
        if os.path.exists(self.filename):
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # Skip empty rows
                        tasks.append(ToDo(row[0], row[1], row[2]))
        return tasks
    
    def save_tasks(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow([task.name, task.priority, task.status])
    
    def add_task(self, name, priority, status="Pending"):
        new_task = ToDo(name, priority, status)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"'{name}' task added successfully!")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks in your to-do list.")
            return
        
        print("\nYour To-Do List:")
        print("-" * 50)
        print(f"{'No.':<5}{'Task':<20}{'Priority':<15}{'Status':<10}")
        print("-" * 50)
        for i, task in enumerate(self.tasks, 1):
            print(f"{i:<5}{task.name:<20}{task.priority:<15}{task.status:<10}")
        print()
    
    def delete_task(self, task_number):
        try:
            task_index = int(task_number) - 1
            if 0 <= task_index < len(self.tasks):
                removed_task = self.tasks.pop(task_index)
                self.save_tasks()
                print(f"Task '{removed_task.name}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    
    def mark_complete(self, task_number):
        try:
            task_index = int(task_number) - 1
            if 0 <= task_index < len(self.tasks):
                self.tasks[task_index].status = "Completed"
                self.save_tasks()
                print(f"Task '{self.tasks[task_index].name}' marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    todo = ToDoList()
    
    while True:
        print("\n" + "=" * 50)
        print("To-Do List Manager (CSV Version)".center(50))
        print("=" * 50)
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Exit")
        print("=" * 50)
        
        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
                todo.view_tasks()
            elif choice == 2:
                name = input("Enter the task: ")
                priority = input("Priority (Low/Normal/High): ").capitalize()
                while priority not in ["Low", "Normal", "High"]:
                    print("Invalid priority! Please enter Low, Normal, or High")
                    priority = input("Priority (Low/Normal/High): ").capitalize()
                todo.add_task(name, priority)
            elif choice == 3:
                todo.view_tasks()
                if todo.tasks:
                    task_num = input("Enter task number to delete: ")
                    todo.delete_task(task_num)
            elif choice == 4:
                todo.view_tasks()
                if todo.tasks:
                    task_num = input("Enter task number to mark as complete: ")
                    todo.mark_complete(task_num)
            elif choice == 5:
                print("Thank you for using the To-Do List System!")
                break
            else:
                print("Invalid choice. Please enter a number between 1-5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "_main_":
    main()