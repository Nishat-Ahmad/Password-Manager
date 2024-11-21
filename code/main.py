import login
import functions
import generator
import checker
import log

# UserName: ab, Password: 12

def main() -> None:
    '''Controls the execution of the whole code.'''
    log.Functions.createFile()
    loginSuccess = login.Login.Login()
    
    if not loginSuccess: 
        print("Login was not successful.")
        return
    else: print("Login was successful.")
    
    while True:
        print("----- Enter -----")
        print("0 to exit")
        print("1 to change master password or user name.")
        print("2 to go to generate custom passwords.")
        print("3 to add, delete, read, or update stored passwords.")
        print("4 to check strength of stored passwords.")
        print("-----------------")
        
        while True:
            try:    choice = int(input("Enter choice here: "))
            except ValueError:
                print("Please enter an integer.")
                log.Functions.mainError(1)
            else:   break
        
        match choice:
            case 0: break
            case 1: login.Login.runner()
            case 2: generator.Generator.runner()
            case 3: functions.runner()
            case 4: checker.runner()
            case _: print("Wrong input.")

if __name__ == "__main__":
    main()