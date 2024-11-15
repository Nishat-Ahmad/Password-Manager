'''
Has add, read, delete, and update functions for data.csv
'''

import csv
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

_path = '../Password Manager/data/data.csv'
_keyPath = '../Password Manager/data/key.txt'
cipher = ""

def runner() -> None:
    while True:
        print("Enter")
        print("0 to exit")
        print("1 to add a new entry.")
        print("2 to read entry.")
        print("3 to update entry.")
        print("4 to delete entry.")
        choice = int(input("Enter here: "))
        
        match choice:
            case 0: break
            case 1:
                account = input("Enter account name: ")
                userName = input("Enter user name: ")
                password = input("Enter password: ")
                note = input("Enter addition note [Enter 'no' if no note]: ")
                if note == 'no':   Add.addEntry(account, userName, password)
                else:               Add.addEntry(account, userName, password, note)
            case 2:
                print("Enter 1 to read full file: ")
                print("Enter 2 for custom search: ")
                choiceRead = int(input("Enter here: "))
                if choiceRead == 1: Read.readFullFile()
                elif choiceRead == 2:
                    print("Enter 1 to search using account, 2 for user name, 3 for password, 4 for note: ")
                    position = int(input("Enter choice here: "))
                    key = input("Enter search term here: ")
                    Read.groupSpecialValues(key, position)
            case 3:
                account = input("Enter account name: ")
                userName = input("Enter user name: ")
                password = input("Enter password: ")
                position = int(input("Enter 1 to change user name, 2 for password: "))
                
                if position == 1: newVal = input("Enter new user name: ")
                elif position == 2: newVal = input("Enter new password: ")
                else: 
                    print("Wrong value input.") 
                    continue
                Update.updateValue(account, userName, password, newVal, position)
            case 4:
                print("Enter 1 to delete 1 user: ")
                print("Enter 2 to delete a bunch using key word: ")
                choiceRead = int(input("Enter here: "))
                if choiceRead == 1:     
                    account = input("Enter account name to delete: ")
                    userName = input("Enter user name to delete: ")
                    password = input("Enter password to delete: ")
                    Delete.deleteEntryFullInfo(account, userName, password)
                elif choiceRead == 2:
                    print("Enter 1 to delete using account, 2 for user name, 3 for password: ")
                    position = int(input("Enter choice here: "))
                    key = input("Enter the value to delete here: ")
                    Delete.deleteAllAccountUser(key, position - 1)
            case _:
                print("Wrong value.")

def load_cipher():
    global cipher
    with open(_keyPath, 'r') as keyfile:
        key = keyfile.read().strip()        # Read and strip any extra whitespace
        cipher = Fernet(key)                # Initialize the Fernet cipher with the key
load_cipher()

class Add:
    def addEntry(account : str, userName : str, password : str, note : str = "No note.") -> None:
        '''
        Adds an entry in the data.csv file.
        '''
        encryptedUserName = cipher.encrypt(userName.encode())
        encryptedPassword = cipher.encrypt(password.encode())
        
        listToAppend = [account, encryptedUserName.decode(), encryptedPassword.decode(), note]
        with open(_path, 'a', newline = "") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(listToAppend)

class Delete:
    def deleteEntryFullInfo(account : str, userName : str, password : str) -> None:
        '''
        Deletes 1 specific entry.
        '''
        listWithRows = []
        with open(_path, 'r') as csvfile:
            for row in csv.reader(csvfile):
                if not (row[0] == account and cipher.decrypt(row[1].encode()).decode() == userName and 
                        cipher.decrypt(row[2].encode()).decode() == password):
                    listWithRows.append(row)
        
        with open(_path, 'w', newline = "") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(listWithRows)
    
    def deleteAllAccountUser(key : str, position : int) -> None:
        '''
        Deletes all the rows with matching position.
        '''
        listWithRows = []
        with open(_path, 'r') as csvfile:
            for row in csv.reader(csvfile):
                if position == 0:
                    if not (row[position] == key):
                        listWithRows.append(row)
                elif position == 1 or position == 2:
                    if not (cipher.decrypt(row[position]).decode() == key):
                        listWithRows.append(row)
                else:
                    print("Wrong input.")
            
        with open(_path, 'w', newline = "") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(listWithRows)

class Read:
    def readFullFile() -> None:
        '''
        It reads the whole file and outputs it in the terminal.
        '''
        index = 1
        with open(_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for corpName, userName, password, note in csv_reader:
                print(f"{index}. {corpName}, {cipher.decrypt(userName).decode()}, {cipher.decrypt(password).decode()}, {note}")
                index += 1
    
    def groupSpecialValues(value : str, position : int) -> None:
        '''
        It reads rows that have similar values to value parameter and outputs them.
        '''
        index = 1
        with open(_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if position == 0 or position == 3:
                    if value == row[position]:
                        print(f"{index}. {row[0]}, {cipher.decrypt(row[1]).decode()}, {cipher.decrypt(row[2]).decode()}, {row[3]}")
                        index += 1
                elif position == 1 or position == 2:    # Just to check username or password.
                    if value == cipher.decrypt(row[position]).decode():
                        print(f"{index}. {row[0]}, {cipher.decrypt(row[1]).decode()}, {cipher.decrypt(row[2]).decode()}, {row[3]}")
                        index += 1
                else:   print("Wrong position entered. [149, functions.py]")

class Update:
    def updateValue(account : str, userName : str, password : str, valueToUpdate : str, position : int) -> None:
        '''
        Update username or password or note.
        '''
        listWithRows = []
        with open(_path, 'r') as csvfile:
            for row in csv.reader(csvfile):
                listWithRows.append(row)
            
        for row in listWithRows:
            try:
                if (row[0] == account and cipher.decrypt(row[1].encode()).decode() == userName and cipher.decrypt(row[2].encode()).decode() == password):
                    encryptedValueToUpdate = cipher.encrypt(valueToUpdate.encode())
                    row[position] = encryptedValueToUpdate.decode()
                    
            except InvalidToken:    pass # As invalid tokens are going to be generated.
            
        # Rewites the list into .csv file
        with open(_path, 'w', newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(listWithRows)