from tasks import todo_list, create_task, delete_task, mark_as_finished, delete_all_tasks, view_all_tasks
from accounts import accounts, add_account, login 

def logsin(name, password):
    if login(name, password) is True:
        manup()

        
    else:
        print ("Account does not exist, Please Signup")

def manup():
    print("Provide options:")
    print("1. Create Task")
    print("2. Delete Task ")
    print("3. Mark As Finished")
    print("4. Delete All Tasks")
    print("5. View All Tasks")

    selection = input("Enter selection[1-4]:  ")

    if selection == "1":
        create_task("task")
        manup()

    elif selection == "2":
        delete_task("task")
        manup()

    elif selection == "3":
        mark_as_finished("task")
        manup()

    elif selection == "4":
        delete_all_tasks()
        manup()
    
    elif selection == "5":
        view_all_tasks()
        manup()
    
    else:
        print("Invalid Input")
        manup()

if __name__ == "__main__":

    while True:

        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your Choice: ")

        if choice == "1":
            name = input("Enter New User Name:  ")
            password = input("Enter New User Password:  ")
            add_account(name, password)
            logsin(name, password)
            
            
            
                
        elif choice == "2":# 
            name = input("Enter New User Name:  ")
            password = input("Enter New User Password:  ")
            login(name, password)
            
    
            
        elif choice == "3":
            print("Thank You")
            

        else:
            print("INVALID INPUT")
            

                    


