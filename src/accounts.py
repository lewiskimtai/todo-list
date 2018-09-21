accounts = {}

def add_account(name, password):

   
    #accounts = {name: password}
    accounts[password] = name
    print("Account successfully added")
    
    return accounts


def login(name, password):
    
    
    for key,value in accounts.items():
        if name == value and password == key:
            print("Logged_In Successfully")
            return True
            
        else:
            print("Log_In Unsuccessful")
    return False





