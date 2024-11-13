'''
Has functions to handle login, master password and username.
'''

import hashlib

def hash_message(message: str) -> str:
    hash_object = hashlib.sha256(message.encode())
    return hash_object.hexdigest()  # coverts the binaries to hex value for human readable.

def verify_message(original_hash: str, new_message: str) -> bool:
    new_hash = hash_message(new_message)
    return original_hash == new_hash

class Login:
    __path = "../data/main.txt"
    
    def runner() -> None:
        while True:
            print("-- Enter --")
            print("0 to exit.")
            print("1 to change login password.")
            print("2 to change login user name.")
            choice = (int(input("Enter choice here: ")))
        
            match choice:
                case 0: break
                case 1: 
                    Login.Login()
                    newPassword = input("Enter new password here: ")
                    Login.changePassword(newPassword)
                    print("Password changed successfully.")
                case 2:
                    Login.Login()
                    newUserName = input("Enter new user name here: ")
                    Login.changeUserName(newUserName)
                    print("User name changed successfully.")
                case _:
                    print("Wrong choice.")
    
    def Login() -> None:
        '''
        Runs the loginCheck 5 times.
        '''
        tries = 0
        loginSuccess = False
        while(tries < 5 and loginSuccess == False):
            Name = input("Enter user name: ")
            password = input("Enter password: ")
            loginSuccess = Login.loginCheck(Name, password)
            tries += 1
            if loginSuccess == False:
                print(f"Wrong name or password, tries left: {5 - tries}")

    def loginCheck(name : str, password : str) -> bool:
        '''
        Checks if the argument match the values in the mainPass.txt file.
        '''
        with open(Login.__path, "r") as file:
            data = file.readlines()
            for line in data:
                word = line.split(',')
                if verify_message(word[0], name) and verify_message(word[1], password):
                    print("Successfully logged in.")
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
            appendThis = word[0] + "," + hash_message(newPassword)
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
            appendThis =  hash_message(newName) + "," + word[1]
            file.write(appendThis)