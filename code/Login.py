class Login:
    __path = "../data/main.txt"
    
    def login():
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
                if word[0] == name and word[1] == password:
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
            appendThis = word[0] + "," + newPassword
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
            appendThis =  newName + "," + word[1]
            file.write(appendThis)