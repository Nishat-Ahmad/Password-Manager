import csv

def addEntry(account : str, userName : str, password : str, note : str = "No note.") -> None:
    '''
    Adds an entry in the data.csv file.
    '''
    listToAppend = [account, userName, password, note]
    with open('data.csv', 'a', newline = "") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(listToAppend)
        
def readFullFile() -> None:
    '''
    Adds an entry as a row in the data.csv file.
    '''
    index = 1
    with open('data.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for corpName, userName, password, note in csv_reader:
            print(f"{index}. {corpName}, {userName}, {password}, {note}")
            index += 1

def deleteEntryFullInfo(account : str, userName : str, password : str, note : str = "No note.") -> None:
    '''
    Deletes either 1 or several rows in the data.csv file.
    '''
    listWithRows = []
    with open('data.csv', 'r') as csvfile:
        for row in csv.reader(csvfile):
            if not (row[0] == account and row[1] == userName and row[2] == password and row[3] == note):
                listWithRows.append(row)
    
    with open('data.csv', 'w', newline = "") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(listWithRows)   # Writes rows

def updateAllAccountValue(oldAccount : str, newAccount : str) -> None:
    '''
    Updates all accounts values that are matching to the parameter.
    '''
    listWithRows = []
    with open('data.csv', 'r') as csvfile:
        for row in csv.reader(csvfile):
            listWithRows.append(row)
        
    for row in listWithRows:
        if row[0] == oldAccount:
            row[0] = newAccount
    
    with open('data.csv', 'w', newline = "") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(listWithRows)   # Writes rows