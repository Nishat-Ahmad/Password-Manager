from pathlib import Path
from datetime import datetime

# DEBUG for debugging details.
# INFO for general events.
# WARNING for non-critical issues.
# ERROR for significant problems.
# CRITICAL for serious failures.

class Functions():
    _path = "../Password Manager/logs"
    _logFilePath = ""
    dateTimeVar = datetime.now()
    
    def countFiles(folder_path : str) ->int:
        path = Path(folder_path)  
        return sum(1 for item in path.iterdir() if item.is_file())
    
    def createFile() -> None:
        global _logFilePath
        numOfFiles = Functions.countFiles(Functions._path)
        with open(f"{Functions._path}/{str(Functions.dateTimeVar.date())}-{str((numOfFiles))}.txt", "a") as file:
            _logFilePath = f"{Functions._path}/{str(Functions.dateTimeVar.date())}-{str(numOfFiles)}.txt"
            
    def passwordChecker() -> None:
        with open(_logFilePath, "a") as file:
            file.write(f"{str(Functions.dateTimeVar.date())} - {str(Functions.dateTimeVar.time())} INFO [Password Checker] Password checker was used.\n")
            
    def login(trigger : int) -> None:
        timeNow = datetime.now()
        with open(_logFilePath, "a") as file:
            match trigger:
                case 1: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} DEBUG [Login] Login attempted.\n")
                case 2: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} INFO [Login] Successfully logged in.\n")
                case 3: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} DEBUG [Login] Failed to login.\n")
                case 4: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} INFO [Login]  Master password has been changed.\n")
                case 5: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} INFO [Login] Master user name has been changed.\n")
    
    def loginError(trigger : int) -> None:
        timeNow = datetime.now()
        with open(_logFilePath, "a") as file:
            match trigger:
                case 1: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} ERROR [Login] Value error in 'choice' [line 24].\n")
                
    def mainError(trigger : int) -> None:
        timeNow = datetime.now()
        with open(_logFilePath, "a") as file:
            match trigger:
                case 1: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} ERROR [MAIN] Value error in 'choice' [line 27].\n")
    

    def generator(trigger : int) -> None:
        timeNow = datetime.now()
        with open(_logFilePath, "a") as file:
            match trigger:
                case 1: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} INFO [Generator] Password generator was accessed.\n")
                case 2: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} INFO [Generator] Fully random password generator was used.\n")
                case 3: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} INFO [Generator] Custom random password generator was used.\n")
    
    def generatorError(trigger : int) -> None:
        timeNow = datetime.now()
        with open(_logFilePath, "a") as file:
            match trigger:
                case 1: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} ERROR [Generator] Value error in 'choice' [line 25].\n")
                case 2: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} ERROR [Generator] Value error in 'choice' [line 46].\n")
                case 3: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} ERROR [Generator] Value error in 'remove' [line 55].\n")
                case 4: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} ERROR [Generator] Value error in 'remove' [line 32].\n")
                case 'start': file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} ERROR [Generator] Value error in 'start' [line 75].\n")
                case 'end': file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} ERROR [Generator] Value error in 'end' [line 82].\n")

    def functions(trigger : int) -> None:
        timeNow = datetime.now()
        with open(_logFilePath, "a") as file:
            match trigger:
                case 1: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} INFO [Functions] New data was added.\n")
                case 2: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} INFO [Functions] All of data.csv was read.\n")
                case 3: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} INFO [Functions] Part of data.csv was read.\n")
                case 4: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} WARNING [Functions] Part of data.csv was updated.\n")
                case 5: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} WARNING [Functions] Data of one user was deleted.\n")
                case 6: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} WARNING [Functions] Data of a bunch of users was deleted.\n")
    
    def functionsError(trigger : int) -> None:
        timeNow = datetime.now()
        with open(_logFilePath, "a") as file:
            match trigger:
                case 1: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} ERROR [Functions] Value error in 'choice' [line 27].\n")
                case 2: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} ERROR [Functions] Value error in 'choiceRead' [line 45].\n")
                case 3: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} ERROR [Functions] Value error in 'position' [line 57].\n")
                case 4: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} ERROR [Functions] Value error in 'position' [line 72].\n")
                case 5: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} ERROR [Functions] Value error in 'position' [line 89].\n")
                case 6: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} ERROR [Functions] Value error in 'position' [line 105].\n")
                case 7: file.write(f"{str(Functions.dateTimeVar.date())} - {str(timeNow.time())} ERROR [Functions] Invalid Token [line 220].\n")