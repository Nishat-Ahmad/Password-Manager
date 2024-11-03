import Login

def login():
    tries = 0
    loginSuccess = False
    while(tries < 5 and loginSuccess == False):
        Name = input("Enter name: ")
        password = input("Enter password: ")
        loginSuccess = Login.login(Name, password)
        tries += 1
        if loginSuccess == False:
            print(f"Wrong name or password, tries left: {5 - tries}")

login()
Login.changePassword("12345")
login()