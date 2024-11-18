import Login
import functions
import generator
import passChecker
import log

# UserName: ab, Password: 123

def main() -> None:
    log.Functions.createFile()
    loginSuccess = Login.Login.Login()
    
    if not loginSuccess: 
        print("Login was not successful.")
        return
    else: print("Login was successful.")
    
    while True:
        print("Enter:")
        print("0 to exit")
        print("1 to go to Login")
        print("2 to go to password generator")
        print("3 to add, delete, read, or update stored passwords")
        print("4 to check strength of passwords that are stored")
        
        while True:
            try:    choice = int(input("Enter choice here: "))
            except ValueError:
                print("Please enter an integer.")
                log.Functions.mainError(1)
            else:   break
        
        match choice:
            case 0: break
            case 1: Login.Login.runner()
            case 2: generator.Generator.runner()
            case 3: functions.runner()
            case 4: passChecker.runner()
            case _: print("Wrong input")

if __name__ == "__main__":
    main()