'''
Has add, read, delete, and update functions for data.csv
'''

import csv

_path = '../data/data.csv'

def runner() -> None:
    while True:
        print("Enter")
        print("0 to exit")
        print("1 to add a new entry.")
        print("2 to red entry.")
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
                account = input("Enter account name: ")
                userName = input("Enter user name: ")
                password = input("Enter password: ")
                
                print("Enter 1 to delete 1 user: ")
                print("Enter 2 to delete a bunch using key word: ")
                choiceRead = int(input("Enter here: "))
                if choiceRead == 1:     Delete.deleteEntryFullInfo(account, userName, password)
                elif choiceRead == 2:
                    print("Enter 1 to delete using account, 2 for user name, 3 for password: ")
                    position = int(input("Enter choice here: "))
                    key = input("Enter dlete item key here: ")
                    Delete.deleteAllAccountUser(key, position)                
            case _:
                print("Wrong value.")
                
class Add:
    def addEntry(account : str, userName : str, password : str, note : str = "No note.") -> None:
        '''
        Adds an entry in the data.csv file.
        '''
        listToAppend = [account, userName, password, note]
        with open(_path, 'a', newline = "") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(listToAppend)

class Delete:
    def deleteEntryFullInfo(account : str, userName : str, password : str, note : str = "No note.") -> None:
        '''
        Deletes 1 specific entry.
        '''
        listWithRows = []
        with open(_path, 'r') as csvfile:
            for row in csv.reader(csvfile):
                if not (row[0] == account and row[1] == userName and row[2] == password and row[3] == note):
                    listWithRows.append(row)
        
        with open(_path, 'w', newline = "") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(listWithRows)   # Writes rows
    
    def deleteAllAccountUser(key : str, position : int) -> None:
        '''
        Deletes all the rows with matching position.
        '''
        listWithRows = []
        with open(_path, 'r') as csvfile:
            for row in csv.reader(csvfile):
                if not (row[position] == key):
                    listWithRows.append(row)
        
        with open(_path, 'w', newline = "") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(listWithRows)   # Writes rows

class Read:
    def readFullFile() -> None:
        '''
        It reads the whole file and outputs it in the terminal.
        '''
        index = 1
        with open(_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for corpName, userName, password, note in csv_reader:
                print(f"{index}. {corpName}, {userName}, {password}, {note}")
                index += 1
    
    def groupSpecialValues(value : str, position : int) -> None:
        '''
        It reads rows that have similar values to value parameter and outputs them.
        '''
        index = 1
        with open(_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if value == row[position]:
                    print(f"{index}. {row[0]}, {row[1]}, {row[2]}, {row[3]}")
                    index += 1

class Update:
    def updateValue(account : str, userName : str, password : str, valueToUpdate : str, position : int) -> None:
        '''
        Update username or password or note.
        '''
        listWithRows = []
        with open(_path, 'r') as csvfile:
            for row in csv.reader(csvfile):
                listWithRows.append(row)
            
        # Finds the row which matches account, username and password.
        for row in listWithRows:
            if row[0] == account and row[1] == userName and row[2] == password:
                row[position] = valueToUpdate
        
        # Rewites the list into .csv file
        with open(_path, 'w', newline = "") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(listWithRows)   # Writes rows