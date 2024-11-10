import csv

class Add:
    def addEntry(account : str, userName : str, password : str, note : str = "No note.") -> None:
        '''
        Adds an entry in the data.csv file.
        '''
        listToAppend = [account, userName, password, note]
        with open('data.csv', 'a', newline = "") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(listToAppend)

class Delete:
    def deleteEntryFullInfo(account : str, userName : str, password : str, note : str = "No note.") -> None:
        '''
        Deletes 1 specific entry.
        '''
        listWithRows = []
        with open('data.csv', 'r') as csvfile:
            for row in csv.reader(csvfile):
                if not (row[0] == account and row[1] == userName and row[2] == password and row[3] == note):
                    listWithRows.append(row)
        
        with open('data.csv', 'w', newline = "") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(listWithRows)   # Writes rows
    
    def deleteAllAccount(account : str) -> None:
        '''
        Deletes all the rows with account matching "account".
        '''
        listWithRows = []
        with open('data.csv', 'r') as csvfile:
            for row in csv.reader(csvfile):
                if not (row[0] == account):
                    listWithRows.append(row)
        
        with open('data.csv', 'w', newline = "") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(listWithRows)   # Writes rows
            
    def deleteAllUsers(userName : str) -> None:
        '''
        Deletes all the rows with username matching "userName".
        '''
        listWithRows = []
        with open('data.csv', 'r') as csvfile:
            for row in csv.reader(csvfile):
                if not (row[1] == userName):
                    listWithRows.append(row)
        
        with open('data.csv', 'w', newline = "") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(listWithRows)   # Writes rows

class Read:
    def readFullFile() -> None:
        '''
        It reads the whole file and outputs it in the terminal.
        '''
        index = 1
        with open('data.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for corpName, userName, password, note in csv_reader:
                print(f"{index}. {corpName}, {userName}, {password}, {note}")
                index += 1
    
    def groupSpecialValues(value : str, position : int) -> None:
        '''
        It reads rows that have similar values to value parameter and outputs them.
        '''
        index = 1
        with open('data.csv', 'r') as csvfile:
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
        with open('data.csv', 'r') as csvfile:
            for row in csv.reader(csvfile):
                listWithRows.append(row)
            
        # Finds the row which matches account, username and password.
        for row in listWithRows:
            if row[0] == account and row[1] == userName and row[2] == password:
                row[position] = valueToUpdate
        
        # Rewites the list into .csv file
        with open('data.csv', 'w', newline = "") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(listWithRows)   # Writes rows