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
            file.write(f"{str(Functions.dateTime.date())} INFO [Password Checker] {str(Functions.dateTime.time())} Password checker was used.\n")
            
    def login(trigger : int) -> None:
        with open(_logFilePath, "a") as file:
            match trigger:
                case 1: file.write(f"{str(Functions.dateTime.date())} DEBUG [Login] {str(Functions.dateTime.time())} Login attempted.\n")
                case 2: file.write(f"{str(Functions.dateTime.date())} INFO [Login] {str(Functions.dateTime.time())} Successfully logged in.\n")
                case 3: file.write(f"{str(Functions.dateTime.date())} DEBUG [Login] {str(Functions.dateTime.time())} Failed to login.\n")
                case 4: file.write(f"{str(Functions.dateTime.date())} INFO [Login] {str(Functions.dateTime.time())} Master password has been changed.\n")
                case 5: file.write(f"{str(Functions.dateTime.date())} INFO [Login] {str(Functions.dateTime.time())} Master user name has been changed.\n")

    def generator(trigger : int) -> None:
        with open(_logFilePath, "a") as file:
            match trigger:
                case 1: file.write(f"{str(Functions.dateTime.date())} INFO [Generator] {str(Functions.dateTime.time())} Password generator was accessed.\n")
                case 2: file.write(f"{str(Functions.dateTime.date())} INFO [Generator] {str(Functions.dateTime.time())} Fully random password generator was used.\n")
                case 3: file.write(f"{str(Functions.dateTime.date())} INFO [Generator] {str(Functions.dateTime.time())} Custom random password generator was used.\n")

    def functions(trigger : int) -> None:
        with open(_logFilePath, "a") as file:
            match trigger:
                case 1: file.write(f"{str(Functions.dateTime.date())} INFO [Functions] {str(Functions.dateTime.time())} New data was added.\n")
                case 2: file.write(f"{str(Functions.dateTime.date())} INFO [Functions] {str(Functions.dateTime.time())} All of data.csv was read.\n")
                case 3: file.write(f"{str(Functions.dateTime.date())} INFO [Functions] {str(Functions.dateTime.time())} Part of data.csv was read.\n")
                case 4: file.write(f"{str(Functions.dateTime.date())} WARNING [Functions] {str(Functions.dateTime.time())} Part of data.csv was updated.\n")
                case 5: file.write(f"{str(Functions.dateTime.date())} WARNING [Functions] {str(Functions.dateTime.time())} Data of one user was deleted.\n")
                case 6: file.write(f"{str(Functions.dateTime.date())} WARNING [Functions] {str(Functions.dateTime.time())} Data of a bunch of users was deleted.\n")