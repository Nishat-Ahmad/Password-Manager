'''Has add, read, delete, and update functions for data.csv'''

import csv
import log
import login
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

_path = '../Password Manager/data/data.csv'
_keyPath = '../Password Manager/data/key.txt'
cipher = ""

def runner() -> None:
    '''Runs all the add, delete, update and read functions.'''
    load_cipher()
    
    while True:
        print("----- Enter -----")
        print("0 to exit")
        print("1 to add a new entry.")
        print("2 to read entry.")
        print("3 to update entry.")
        print("4 to delete entry.")
        print("-----------------")
        
        # Entering choice.
        choice = chooseValue(1)
        
        match choice:
            case 0: break
            case 1: # Adding a new entry.
                print("----------")
                account = input("Enter account name: ")
                userName = input("Enter user name: ")
                password = input("Enter password: ")
                note = input("Enter addition note [Enter 'no' if no note]: ")
                print("----------")
                if note == 'no':   Add.addEntry(account, userName, password)
                else:               Add.addEntry(account, userName, password, note)
                log.Functions.functions(1)
                
            case 2: # Reading the entries.
                print("----------")
                print("Enter master credentials:")
                loginSuccess = login.Login.Login()
                if not(loginSuccess): 
                    print("Invalid master credentials were logged, failed to read file.")
                    break
                
                print("----------")
                print("Enter 1 to read full file: ")
                print("Enter 2 for custom search: ")
                print("----------")
                
                choiceRead = chooseValue(2)
                
                if choiceRead == 1:
                    print("---------------") 
                    Read.readFullFile()
                    print("---------------") 
                    log.Functions.functions(2)
                    
                elif choiceRead == 2:
                    print("---------------")
                    print("Enter 1 to search using account, 2 for user name, 3 for password, 4 for note: ")
                    print("---------------") 
                    
                    position = chooseValue(3)
                        
                    key = input("Enter search term here: ")
                    Read.groupSpecialValues(key, position - 1)
                    log.Functions.functions(3)
                    
            case 3: # Updating the entry.
                print("---------------") 
                account = input("Enter account name: ")
                userName = input("Enter user name: ")
                password = input("Enter password: ")
                print("---------------")
                
                # Inputting which value to update.
                while True:
                    try:    
                        print("---------------") 
                        position = int(input("Enter 1 to change user name, 2 for password, 3 for account name: "))
                        print("---------------") 
                    except ValueError:
                        print("Please enter an integer.")
                        log.Functions.functionsError(4)
                    else:   break
                print("---------------") 
                
                if position == 1: newVal = input("Enter new user name: ")
                elif position == 2: newVal = input("Enter new password: ")
                elif position == 3: newVal = input("Enter new account name: ")
                else: 
                    print("Wrong value input.") 
                    continue
                
                Update.updateValue(account, userName, password, newVal, position)
                log.Functions.functions(4)
                print("---------------") 
                
            case 4: # Deleting the entry.
                print("---------------") 
                print("Enter 1 to delete only 1 accounts data: ")
                print("Enter 2 to delete a bunch using key word: ")
                print("---------------") 
                
                choiceRead = chooseValue(5)
                
                if choiceRead == 1:     
                    print("---------------") 
                    account = input("Enter account name to delete: ")
                    userName = input("Enter user name to delete: ")
                    password = input("Enter password to delete: ")
                    print("---------------") 
                    
                    Delete.deleteEntryFullInfo(account, userName, password)
                    log.Functions.functions(5)
                    
                elif choiceRead == 2:
                    print("---------------") 
                    print("Enter 1 to delete using account, 2 for user name, 3 for password: ")
                    print("---------------") 
                    
                    position = chooseValue(6)
                    key = input("Enter the value to delete here: ")
                    Delete.deleteAllAccountUser(key, position - 1)
                    log.Functions.functions(6)
                    
            case _: print("Wrong value.")

def load_cipher() -> None:
    '''Loads cipher into 'cipher' from main.txt.'''
    global cipher
    with open(_keyPath, 'r') as keyfile:
        key = keyfile.read().strip()        # Read and strip any extra whitespace
        cipher = Fernet(key)                # Initialize the Fernet cipher with the key

def chooseValue(errorValue : int) -> int:
    '''Checks if value entered is integer.'''
    while True:
        try:    choiceRead = int(input("Enter here: "))
        except ValueError:
            print("Please enter an integer.")
            log.Functions.functionsError(errorValue)
        else:   break
    
    return choiceRead

class Add:
    def addEntry(account : str, userName : str, password : str, note : str = "No note.") -> None:
        '''Adds an entry in the data.csv file.'''
        encryptedUserName = cipher.encrypt(userName.encode())
        encryptedPassword = cipher.encrypt(password.encode())
        
        listToAppend = [account, encryptedUserName.decode(), encryptedPassword.decode(), note]
        with open(_path, 'a', newline = "") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(listToAppend)

class Delete:
    def deleteEntryFullInfo(account : str, userName : str, password : str) -> None:
        '''Deletes 1 specific entry.'''
        listWithRows = []   # Holds all the data.
        with open(_path, 'r') as csvfile:
            for row in csv.reader(csvfile):
                if not (row[0] == account and cipher.decrypt(row[1].encode()).decode() == userName and 
                        cipher.decrypt(row[2].encode()).decode() == password):
                    listWithRows.append(row)
        
        with open(_path, 'w', newline = "") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(listWithRows)
    
    def deleteAllAccountUser(key : str, position : int) -> None:
        '''Deletes all the rows with matching position.'''
        listWithRows = []   # Holds all the data.
        with open(_path, 'r') as csvfile:
            for row in csv.reader(csvfile):
                if position == 0:
                    if not (row[position] == key):
                        listWithRows.append(row)
                elif position == 1 or position == 2:
                    if not (cipher.decrypt(row[position]).decode() == key):
                        listWithRows.append(row)
                else:   print("Wrong input.")
            
        # (newline = "") Windows generate an empty line if this is not written b/w lines.
        with open(_path, 'w', newline = "") as csvfile: # Writing back into the whole file.
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(listWithRows)

class Read:
    def readFullFile() -> None:
        '''It reads the whole file and outputs it in the terminal.'''
        index = 1
        with open(_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for account, userName, password, note in csv_reader:
                print(f"{index}. {account}, {cipher.decrypt(userName).decode()}, {cipher.decrypt(password).decode()}, {note}")
                index += 1
    
    def groupSpecialValues(value : str, position : int) -> None:
        '''It reads rows that have similar values to value parameter and outputs them.'''
        index = 1
        with open(_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if position == 0 or position == 3:      # Checks account / note.
                    if value == row[position]:
                        print(f"{index}. {row[0]}, {cipher.decrypt(row[1]).decode()}, {cipher.decrypt(row[2]).decode()}, {row[3]}")
                        index += 1
                elif position == 1 or position == 2:    # Checks username / password.
                    if value == cipher.decrypt(row[position]).decode():
                        print(f"{index}. {row[0]}, {cipher.decrypt(row[1]).decode()}, {cipher.decrypt(row[2]).decode()}, {row[3]}")
                        index += 1
                else:   print("Wrong position entered. [149, functions.py]")

class Update:
    def updateValue(account : str, userName : str, password : str, valueToUpdate : str, position : int) -> None:
        '''Update username or password or note.'''
        listWithRows = []
        with open(_path, 'r') as csvfile:   # Copying the whole file into listWithRows[].
            for row in csv.reader(csvfile): listWithRows.append(row)
            
        for row in listWithRows:
            try:
                if position == 1 or position == 2:
                    if (row[0] == account and cipher.decrypt(row[1].encode()).decode() == userName and cipher.decrypt(row[2].encode()).decode() == password):
                        encryptedValueToUpdate = cipher.encrypt(valueToUpdate.encode())
                        row[position] = encryptedValueToUpdate.decode()
                elif position == 3: # Updates the account name.
                    if (row[0] == account and cipher.decrypt(row[1].encode()).decode() == userName and cipher.decrypt(row[2].encode()).decode() == password):
                        row[0] = valueToUpdate
                    
            except InvalidToken:    log.Functions.functions(7)
            
        with open(_path, 'w', newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(listWithRows)