import Login
import functions
import generator

# UserName: abc, Password: 123456789

def main() -> None:
    loginSuccess = Login.Login.Login()
    if not loginSuccess: return
    
    while True:
        print("Enter:")
        print("0 to exit")
        print("1 to go to Login")
        print("2 to go to password generator")
        print("3 to add, delete, read, or update stored passwords")
        choice = int(input("Enter choice here: "))
        
        match choice:
            case 0: break
            case 1: Login.Login.runner()
            case 2: generator.Generator.runner()
            case 3: functions.runner()
            case _: print("Wrong input")

main()