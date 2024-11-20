'''
Checks how strong the passwords are that are stored inside the data.csv file.
'''
import csv
import login
import string
import log
from cryptography.fernet import Fernet

_path = '../Password Manager/data/data.csv'
_keyPath = '../Password Manager/data/key.txt'
cipher = ""

def runner() -> None:
    '''Controls the execution of the password checker funtions.'''
    print("-----------------")
    print("Re-Enter login credentials:")
    loginSuccess = login.Login.Login()
    if not(loginSuccess):
        print("Failed to login.")
        print("-----------------")
        return
    
    print("-----------------")
    PassCheck.dataTransferList()
    log.Functions.passwordChecker()
    PassCheck.output()

# Loads the cipher so that it can be used for decoding.
def load_cipher():
    global cipher
    with open(_keyPath, 'r') as keyfile:
        key = keyfile.read().strip()        # Read and strip any extra whitespace
        cipher = Fernet(key)                # Initialize the Fernet cipher with the key
load_cipher()

class PassCheck:
    values = []     # Contains all the values after decoding.
    
    def dataTransferList() -> None:
        '''Moves data from data.csv to values[]'''
        index = 1
        with open(_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for corpName, userName, password, note in csv_reader:
                PassCheck.values.append(corpName)
                PassCheck.values.append(cipher.decrypt(userName).decode())
                PassCheck.values.append(cipher.decrypt(password).decode())
                PassCheck.values.append(note)
                
                index += 1
    
    def containDigits(ValString : str) -> bool:
        ''' Checks if the password have at least 1 digit in it.'''
        val = list(ValString)
        digits = list(string.digits)
        if any(word in val for word in digits): return True
        else: return False

    def containLowerCase(ValString : str) -> bool:
        ''' Checks if the password have at least 1 lower case chracter in it.'''
        val = list(ValString)
        lowercaseLetters = list(string.ascii_lowercase)
        if any(word in val for word in lowercaseLetters): return True
        else: return False
    
    def containUpperCase(ValString : str) -> bool:
        ''' Checks if the password have at least 1 upper case chracter in it.'''
        val = list(ValString)
        uppercaseLetters = list(string.ascii_uppercase)
        if any(word in val for word in uppercaseLetters): return True
        else: return False
        
    def containSpecialChracters(ValString : str) -> bool:
        ''' Checks if the password have at least 1 special chracter in it.'''
        val = list(ValString)
        specialCharacters = list("!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~")
        if any(word in val for word in specialCharacters): return True
        else: return False
    
    def output():
        '''Prints all the insight of the password one by one.'''
        for i in range(0, len(PassCheck.values), 4):
            print("--------------------------------------------------")
            print(f"Account Type: {PassCheck.values[i]} - Account user Name: {PassCheck.values[i + 1]}")
            if len(PassCheck.values[i + 2]) > 12:   print("Password is more than 12 chracters.")
            else:   print("Password is less than 12 chracters.")
            if PassCheck.containDigits(PassCheck.values[i + 2]): print("Password contains atleast one digit.")
            else: print("Password does not contain even one digit.")
            if PassCheck.containLowerCase(PassCheck.values[i + 2]): print("Password contains atleast one lower case letter.")
            else: print("Password does not contain even one lower case letter.")
            if PassCheck.containUpperCase(PassCheck.values[i + 2]): print("Password contains atleast one upper case letter.")
            else: print("Password does not contain even one upper case letter.")
            if PassCheck.containSpecialChracters(PassCheck.values[i + 2]): print("Password contains atleast one special chracter.")
            else: print("Password does not contain even one special chracter.")