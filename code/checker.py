'''Checks how strong the passwords are that are stored inside the data.csv file.'''
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
    
    loadCipher()
    PassCheck.dataTransferList()
    log.Functions.passwordChecker()
    PassCheck.output()

# Loads the cipher so that it can be used for decoding.
def loadCipher():
    '''Loads cipher from key.txt into 'cipher' variable.'''
    global cipher
    with open(_keyPath, 'r') as keyfile:
        key = keyfile.read().strip()        # Read and strip any extra whitespace
        cipher = Fernet(key)                # Initialize the Fernet cipher with the key

class PassCheck:
    values = []     # Contains all the rows after decoding.
    
    def dataTransferList() -> None:
        '''Copies data from data.csv to values list.'''
        with open(_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for corpName, userName, password, note in csv_reader:
                PassCheck.values.append(corpName)
                PassCheck.values.append(cipher.decrypt(userName).decode())
                PassCheck.values.append(cipher.decrypt(password).decode())
                PassCheck.values.append(note)
    
    # The 4 functions (containDigits, containLowerCase, containUpperCase, containSpecialChracters) are identical.
    def containDigits(ValString : str) -> bool:
        ''' Checks if the password have at least 1 digit in it.'''
        chracterList = list(ValString)
        digits = list(string.digits)
        if any(word in chracterList for word in digits): return True
        else: return False

    def containLowerCase(ValString : str) -> bool:
        ''' Checks if the password have at least 1 lower case chracter in it.'''
        chracterList = list(ValString)
        lowercaseLetters = list(string.ascii_lowercase)
        if any(word in chracterList for word in lowercaseLetters): return True
        else: return False
    
    def containUpperCase(ValString : str) -> bool:
        ''' Checks if the password have at least 1 upper case chracter in it.'''
        chracterList = list(ValString)
        uppercaseLetters = list(string.ascii_uppercase)
        if any(word in chracterList for word in uppercaseLetters): return True
        else: return False
        
    def containSpecialChracters(ValString : str) -> bool:
        ''' Checks if the password have at least 1 special chracter in it.'''
        chracterList = list(ValString)
        specialCharacters = list("!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~")
        if any(word in chracterList for word in specialCharacters): return True
        else: return False
    
    def output():
        '''Prints if a password is passing the checks or not.'''
        for i in range(0, len(PassCheck.values), 4):
            print("--------------------------------------------------")
            print(f"Account Type: {PassCheck.values[i]} - Account user Name: {PassCheck.values[i + 1]}")
            
            if len(PassCheck.values[i + 2]) > 12:                           print("Password is more than 12 chracters.")
            else: print("Password is less than 12 chracters.")
            
            if PassCheck.containDigits(PassCheck.values[i + 2]):            print("Password contains atleast one digit.")
            else: print("Password does not contain even one digit.")
            
            if PassCheck.containLowerCase(PassCheck.values[i + 2]):         print("Password contains atleast one lower case letter.")
            else: print("Password does not contain even one lower case letter.")
            
            if PassCheck.containUpperCase(PassCheck.values[i + 2]):         print("Password contains atleast one upper case letter.")
            else: print("Password does not contain even one upper case letter.")
            
            if PassCheck.containSpecialChracters(PassCheck.values[i + 2]):  print("Password contains atleast one special chracter.")
            else: print("Password does not contain even one special chracter.")