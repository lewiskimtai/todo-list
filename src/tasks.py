todo_list = []

def create_task(task):
    task = input("Create a Task:  ")
    todo_list.append(task)
    print("Task successfully created")
    print(todo_list)
    return

def delete_task(task):
    task = input("Enter the task you want to delete:   ")
    
    if task in todo_list:
        todo_list.remove(task)
        print("Task Successfully Deleted")

    else:
        print("Task not in todo_list. Input a correct task")

def mark_as_finished(task):
    task = input("Input in the Task that you want to mark as FINISHED:  ")

    if task in todo_list:
        print(task + "FINSIHED")
    else:
        print("Task not in todo_list")

def delete_all_tasks():
    todo_list.clear()
    print("All Tasks Successfully Deleted")
