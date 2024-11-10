import Login
import addDeleteReadUpdate as ADRU

ADRU.readFullFile()
ADRU.deleteEntryFullInfo("Google", "nishat", "abce")
ADRU.addEntry("Google", "nishat", "abce")
ADRU.readFullFile()
ADRU.updateAllAccountValue("Google", "Facebook")
ADRU.readFullFile()