from tasks import todo_list, create_task, delete_task, mark_as_finished, delete_all_tasks  # import other functions as well
from accounts import accounts, add_account, login  # import the function as well


if __name__ == "__main__":

    name = input("Enter your name:  ")
    password = input("Enter your password:  ")

    if login(name, password) is True:
        print("Provide options:")
        print("1. creating a task")
        print("2. deleting a task ")
        print("3. deleting all tasks")
        print("4. Marking a task finished")

        selection = input("Enter selection[1-4]:  ")

        if selection == '1':
            create_task("task")

        elif selection == '2':
            delete_task("task")

        elif selection == '3':
            delete_all_tasks()

        elif selection == '4':
            mark_as_finished("task")
        
        else:
            print("Invalid Input")
    
    else:
        print ("Account does not exist, Please Signup")
        add_account("name", "password")
       
    #else:
       # print("Please LogIns")
        #login("name", "password")

        


