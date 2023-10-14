# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    if task not in tasks:
        tasks.append(task)
        print("Task added:", task)
    else:
        print("\033[33mTask already exists : kindly add another task:") 

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("|||||||List of all Tasks|||||")   
        for i, task in enumerate(tasks, start=1):
         print(f"\033[36m{i}. {task}\033[0m")  
# Function to remove a task by index
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print("Task removed:", removed_task)
    else:
         print("\033[33mInvalid task index.\033[0m") 

# Function to update a task by index
def update_task(index, new_task):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = new_task
        print("Task updated:", new_task)
    else:
        print("\033[33mInvalid task index.\033[0m")  


def main():

    while True:
        print('\n')
        print("\033[32m||||||TO DO LIST||||||\033[0m")  
        print("\033[32m1. Add Task\033[0m")          
        print("\033[32m2. List Tasks\033[0m")
        print("\033[32m3. Update Task\033[0m")
        print("\033[32m4. Remove Task\033[0m")
        print("\033[32m5. Quit\033[0m")

        choice = input("Enter your choice:") 
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            index = int(input("Enter the task index to update task: "))
            new_task = input("Enter the new task: ")
            update_task(index, new_task)
        elif choice == '4':
            index = int(input("Enter the task index to remove: "))
            remove_task(index)
        elif choice == '5':
            print("Thank you!!!!") 
            print("Goodbye😊👋!!!!")  

            break
        else:
            print("\033[33mInvalid choice. Please try again.\033[0m")
if __name__ == '__main__':
    main()
