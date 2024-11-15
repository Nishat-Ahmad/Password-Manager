import Login
import functions
import generator
import passChecker

# UserName: abc, Password: 123456789

def main() -> None:
    loginSuccess = Login.Login.Login()
    if not loginSuccess: 
        print("Login was not successful.")
        return
    
    while True:
        print("Enter:")
        print("0 to exit")
        print("1 to go to Login")
        print("2 to go to password generator")
        print("3 to add, delete, read, or update stored passwords")
        print("4 to check strength of passwords that are stored")
        choice = int(input("Enter choice here: "))
        
        match choice:
            case 0: break
            case 1: Login.Login.runner()
            case 2: generator.Generator.runner()
            case 3: functions.runner()
            case 4: passChecker.runner()
            case _: print("Wrong input")

main()