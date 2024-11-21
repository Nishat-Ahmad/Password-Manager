'''All the functionality for generating random passwords.'''
import random
import string
import log

class Generator:
    password = []   # Stores the password as a list of chracters that is being generated.
    
    def runner() -> None:
        '''Runs the whole password generator functionality.'''
        log.Functions.generator(1)  # logs that password generator was used.
        
        while True:
            print("----- Enter -----")
            print("0 to exit to main menu: ")
            print("1 to generate fully random password: ")
            print("2 to customize password: ")
            print("-----------------")
            
            # Repeatedly takes the input choice till an integer is inputted.
            while True:
                try:    choice = (int(input("Enter choice here: ")))
                except ValueError:
                    print("Please enter an integer.")
                    log.Functions.generatorError(1)
                else:   break
                
            if choice == 0: return # Exits to main menu.
            
            elif choice == 1: #  Generates random password.    
                Generator.extendOrNot(4)    # Checks if the current password has to be appended or not.
                log.Functions.generator(2)
                
                Generator.chracters()
                Generator.specialChracters()
                Generator.digits()
                random.shuffle(Generator.password)
                print("------------------------------")
                print(f"Fully random password: {"".join(Generator.password)}")
                print("------------------------------")
                
            elif choice == 2: # Generates fully random password.
                log.Functions.generator(3)
                
                while True:
                    # Takes what values to add to the password.
                    while True:
                        try:
                            print("----- Enter -----")
                            choice = int(input("0 to exit: \n1 to add digits: \n2 to add letters: \n3 to add special chracters: \nEnter value here: "))
                            print("-----------------")
                        except ValueError:
                            print("Please enter an integer.")
                            log.Functions.generatorError(2)
                        else:   break
                        
                    if choice == 0: break

                    Generator.extendOrNot(3)    # Checks if the current password has to be appended or not.
                    replacement = ''
                    if choice == 1: replacement = "digits"
                    elif choice == 2: replacement = "letters"
                    elif choice == 3: replacement = "special chracters"
                    
                    # Define range start for password.
                    while True:
                        try:    start = int(input(f"----------\nEnter what should be minimum number of {replacement} in the password: "))
                        except ValueError:
                            print("Please enter an integer.")
                            log.Functions.generatorError('start')
                        else:   break
                    
                    # Define range end for password.
                    while True:
                        try:    end = int(input(f"Enter what should be maximum number of {replacement} in the password: "))
                        except ValueError:
                            print("Please enter an integer.")
                            log.Functions.generatorError('end')
                        else:   break
                
                    if choice == 1:         Generator.digits(start, end)
                    elif choice == 2:       Generator.chracters(start, end)
                    elif choice == 3:       Generator.specialChracters(start, end)
                    else:                   print("Wrong choice.")
                    
                    if choice == 1 or choice == 2 or choice == 3:
                        random.shuffle(Generator.password)
                        print(f"----------\n{"".join(Generator.password)}\n----------")
                        
            else:   print("Wrong choice.")
        
    def extendOrNot(errorLog : int):
        ''''Clears or extends the password[] list.'''
        while True:
            try:    remove = int(input("-----\nEnter 0 for a new password or 1 to extend the current password: "))
            except ValueError:
                print("Please enter an integer.")
                log.Functions.generatorError(errorLog)
            else:   break
            
        if remove == 0: Generator.password.clear()
    
    def chracters(start : int = 5, end : int = 10) -> None:
        '''start and stop define range of chracters to be included.'''
        # string.ascii_letters: all upper and lower case letters
        for i in range(random.randint(start, end)):
            Generator.password.append(random.choice(list(string.ascii_letters)))
        
    def specialChracters(start : int = 5, end : int = 10) -> None:
        '''Start and stop define range of special chracters to be included.'''
        special_characters = list("!@#$%^&*()-_=+[]}{|;:'\",.<>?/~`")
        for i in range(random.randint(start, end)):
            Generator.password.append(random.choice(special_characters))
    
    def digits(start : int = 5, end : int = 10) -> None:
        '''Start and stop define range of digits to be included.'''
        digits = list("1234567890")
        for i in range(random.randint(start, end)):
            Generator.password.append(random.choice(digits))