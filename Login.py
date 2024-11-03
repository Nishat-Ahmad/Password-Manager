def login(name, password) -> bool:
    '''
    Checks if the argument match the values in the mainPass.txt file
    '''
    with open("mainPass.txt", "r") as file:
        data = file.readlines()
        for line in data:
            word = line.split(',')
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