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
    dateTime = datetime.now()
    
    def countFiles(folder_path : str) ->int:
        path = Path(folder_path)  
        return sum(1 for item in path.iterdir() if item.is_file())
    
    def createFile() -> None:
        global _logFilePath
        numOfFiles = Functions.countFiles(Functions._path)
        with open(f"{Functions._path}/{str(Functions.dateTime.date())}-{str((numOfFiles))}.txt", "a") as file:
            _logFilePath = f"{Functions._path}/{str(Functions.dateTime.date())}-{str(numOfFiles)}.txt"
            
    def passwordChecker() -> None:
        with open(_logFilePath, "a") as file:
            file.write(f"{str(Functions.dateTime.date())} - {str(Functions.dateTime.time())} INFO [Password Checker] Password checker was used.\n")
            
    def login(trigger : int) -> None:
        with open(_logFilePath, "a") as file:
            match trigger:
                case 1: file.write(f"{str(Functions.dateTime.date())} - {str(Functions.dateTime.time())} DEBUG [Login] Login attempted.\n")
                case 2: file.write(f"{str(Functions.dateTime.date())} - {str(Functions.dateTime.time())} INFO [Login] Successfully logged in.\n")
                case 3: file.write(f"{str(Functions.dateTime.date())} - {str(Functions.dateTime.time())} DEBUG [Login] Failed to login.\n")
                case 4: file.write(f"{str(Functions.dateTime.date())} - {str(Functions.dateTime.time())} INFO [Login]  Master password has been changed.\n")
                case 5: file.write(f"{str(Functions.dateTime.date())} - {str(Functions.dateTime.time())} INFO [Login] Master user name has been changed.\n")

    def generator(trigger : int) -> None:
        with open(_logFilePath, "a") as file:
            match trigger:
                case 1: file.write(f"{str(Functions.dateTime.date())} - {str(Functions.dateTime.time())} INFO [Generator] Password generator was accessed.\n")
                case 2: file.write(f"{str(Functions.dateTime.date())} - {str(Functions.dateTime.time())} INFO [Generator] Fully random password generator was used.\n")
                case 3: file.write(f"{str(Functions.dateTime.date())} - {str(Functions.dateTime.time())} INFO [Generator] Custom random password generator was used.\n")

    def functions(trigger : int) -> None:
        with open(_logFilePath, "a") as file:
            match trigger:
                case 1: file.write(f"{str(Functions.dateTime.date())} - {str(Functions.dateTime.time())} INFO [Functions] New data was added.\n")
                case 2: file.write(f"{str(Functions.dateTime.date())} - {str(Functions.dateTime.time())} INFO [Functions] All of data.csv was read.\n")
                case 3: file.write(f"{str(Functions.dateTime.date())} - {str(Functions.dateTime.time())} INFO [Functions] Part of data.csv was read.\n")
                case 4: file.write(f"{str(Functions.dateTime.date())} - {str(Functions.dateTime.time())} WARNING [Functions] Part of data.csv was updated.\n")
                case 5: file.write(f"{str(Functions.dateTime.date())} - {str(Functions.dateTime.time())} WARNING [Functions] Data of one user was deleted.\n")
                case 6: file.write(f"{str(Functions.dateTime.date())} - {str(Functions.dateTime.time())} WARNING [Functions] Data of a bunch of users was deleted.\n")