accounts = {}

def add_account(name, password):

    name = input("Enter New User Name:  ")
    password = input("Enter New User Password:  ")
    accounts = {name: password}
    print("Account successfully added")
    return accounts


def login(name, password):
    name = name
    password = password
    
    for name, password in accounts:
        if name == name and password == password:
            print("Logged_In Successfully")
        else:
            print("Log_In Unsuccessful") 




