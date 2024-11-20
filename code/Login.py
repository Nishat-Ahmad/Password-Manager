'''
Has functions to handle login, master password and username.
'''
import log
import hashlib

def hashMessage(message: str) -> str:
    return (hashlib.sha256(message.encode())).hexdigest() # coverts the binaries to hex value for human readable.

def checkDetails(original_hash: str, new_message: str) -> bool:
    return (original_hash == hashMessage(new_message))

class Login:
    __path = "../Password Manager/data/main.txt"
    
    def runner() -> None:
        while True:
            print("-- Enter --")
            print("0 to exit.")
            print("1 to change login password.")
            print("2 to change login user name.")
            while True:
                try:    choice = (int(input("Enter choice here: ")))
                except ValueError:
                    print("Please enter an integer.")
                    log.Functions.loginError(1)
                else:   break
        
            match choice:
                case 0: break
                case 1: 
                    print("Enter master credentials:")
                    loginSuccess = Login.Login()
                    if not(loginSuccess): 
                        print("Invalid master credentials were logged")
                        print("Password change failed.")
                        break
                    newPassword = input("Enter new password here: ")
                    Login.changePassword(newPassword)
                    log.Functions.login(4)
                    print("Password changed successfully.")
                case 2:
                    print("Enter master credentials:")
                    loginSuccess = Login.Login()
                    if not(loginSuccess): 
                        print("Invalid master credentials were logged")
                        print("User name change failed.")
                        break
                    newUserName = input("Enter new user name here: ")
                    Login.changeUserName(newUserName)
                    log.Functions.login(5)
                    print("User name changed successfully.")
                case _:
                    print("Wrong choice.")
    
    def Login() -> bool:
        '''
        Runs the loginCheck 5 times.
        '''
        tries = 0
        loginSuccess = False
        while(tries < 5 and loginSuccess == False):
            log.Functions.login(1)
            Name = input("Enter user name: ")
            password = input("Enter password: ")
            loginSuccess = Login.loginCheck(Name, password)
            tries += 1
            if loginSuccess == False:
                print(f"Wrong name or password, tries left: {5 - tries}")
                
        if loginSuccess == True:    log.Functions.login(2)
        elif loginSuccess == False:    log.Functions.login(3)
        return loginSuccess

    def loginCheck(name : str, password : str) -> bool:
        '''
        Checks if the argument match the values in the mainPass.txt file.
        '''
        with open(Login.__path, "r") as file:
            data = file.readlines()
            for line in data:
                word = line.split(',')
                if checkDetails(word[0], name) and checkDetails(word[1], password):
                    return True
                
        
        return False

    def changePassword(newPassword : str) -> None:
        '''
        Changes the password in mainPass.txt file.
        '''
        with open(Login.__path, "r") as file:
            data = file.readlines()
            for line in data:
                word = line.split(',')
        
        with open(Login.__path, "w") as file:
            appendThis = word[0] + "," + hashMessage(newPassword)
            file.write(appendThis)

    def changeUserName(newName : str) -> None:
        '''
        Changes the user name in mainPass.txt file.
        '''
        with open(Login.__path, "r") as file:
            data = file.readlines()
            for line in data:
                word = line.split(',')
        
        with open(Login.__path, "w") as file:
            appendThis =  hashMessage(newName) + "," + word[1]
            file.write(appendThis)