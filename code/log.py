from pathlib import Path
from datetime import datetime

def countFiles(folder_path : str) ->int:
    path = Path(folder_path)  
    return sum(1 for item in path.iterdir() if item.is_file())

_path = "../Password Manager/logs"
print(f"Number of files: {countFiles(_path)}")

# Get current local time
dateTime = datetime.now()
print("Current date and time:", dateTime)
print(f"{str(dateTime.date())}-{str(countFiles(_path))}.txt")