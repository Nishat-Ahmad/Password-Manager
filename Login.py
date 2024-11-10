def login():
    tries = 0
    loginSuccess = False
    while(tries < 5 and loginSuccess == False):
        Name = input("Enter user name: ")
        password = input("Enter password: ")
        loginSuccess = loginCheck(Name, password)
        tries += 1
        if loginSuccess == False:
            print(f"Wrong name or password, tries left: {5 - tries}")

def loginCheck(name, password) -> bool:
    '''
    Checks if the argument match the values in the mainPass.txt file
    '''
    with open("mainPass.txt", "r") as file:
        data = file.readlines()
        for line in data:
            word = line.split(',')
            print(word)
            if word[0] == name and word[1] == password:
                print("Successfully logged in.")
                return True
    
    return False

def changePassword(newPassword):
    with open("mainPass.txt", "r") as file:
        data = file.readlines()
        for line in data:
            word = line.split(',')
    
    with open("mainPass.txt", "w") as file:
        appendThis = word[0] + "," + newPassword
        file.write(appendThis)

def changeUserName(newName):
    with open("mainPass.txt", "r") as file:
        data = file.readlines()
        for line in data:
            word = line.split(',')
    
    with open("mainPass.txt", "w") as file:
        appendThis =  newName + "," + word[1]
        file.write(appendThis)