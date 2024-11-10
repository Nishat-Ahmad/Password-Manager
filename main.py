import Login
import addDeleteReadUpdate as ADRU

ADRU.Add.addEntry("Google", "nishat", 'abc')
ADRU.Add.addEntry("Google", "asdfasf", 'abc')
ADRU.Add.addEntry("Google", "xcmvnxc", 'abc')
ADRU.Add.addEntry("Google", "asodfjasd", 'abc')
ADRU.Add.addEntry("Facebook", "asodfjasd", 'abc')
ADRU.Read.readFullFile()
ADRU.Read.groupSpecialValues("Google", 0)