'''
All the functionality for generating random passwords.
'''

import random
import string
import log

class Generator:
    password = []
    
    def runner() -> None:
        '''
        Runs the whole password generator functionality.
        '''
        log.Functions.generator(1)
        while True:
            print("Enter 0 to exit: ")
            print("Enter 1 to generate fully random password: ")
            print("Enter 2 to customize it: ")
            while True:
                try:    choice = (int(input("Enter choice here: ")))
                except ValueError:
                    print("Please enter an integer.")
                    log.Functions.generatorError(1)
                else:   break
                
            if choice == 0:
                return
            elif choice == 1:
                while True:
                    try:    remove = int(input("0 to clear buffer or 1 to keep extending size: "))
                    except ValueError:
                        print("Please enter an integer.")
                        log.Functions.generatorError(4)
                    else:   break
                if remove == 0: Generator.password.clear()

                if remove == 0: Generator.password.clear()
                log.Functions.generator(2)
                
                Generator.chracters()
                Generator.specialChracters()
                Generator.digits()
                random.shuffle(Generator.password)
                print("------------------------------")
                print(f"Fully random password: {"".join(Generator.password)}")
                print("------------------------------")
            elif choice == 2:
                log.Functions.generator(3)
                while True:
                    while True:
                        try:    choice = int(input("Enter 0 to exit: \nEnter 1 to add digits: \nEnter 2 to add letters: \nEnter 3 to add special chracters: \nEnter: "))
                        except ValueError:
                            print("Please enter an integer.")
                            log.Functions.generatorError(2)
                        else:   break
                        
                    if choice == 0: break
                    
                    while True:
                        try:    remove = int(input("Enter 0 to clear buffer and 1 to keep adding to it: "))    
                        except ValueError:
                            print("Please enter an integer.")
                            log.Functions.generatorError(3)
                        else:   break
                    if remove == 0: Generator.password.clear()
                    
                    replacement = ''
                    if choice == 1: replacement = "digits"
                    elif choice == 2: replacement = "letters"
                    elif choice == 3: replacement = "special chracters"
                    
                    while True:
                        try:    start = int(input(f"Enter what should be minimum number of {replacement} in the password: "))
                        except ValueError:
                            print("Please enter an integer.")
                            log.Functions.generatorError('start')
                        else:   break
                    
                    while True:
                        try:    end = int(input(f"Enter what should be maximum number of {replacement} in the password: "))
                        except ValueError:
                            print("Please enter an integer.")
                            log.Functions.generatorError('end')
                        else:   break
                
                    if choice == 1:                    
                        Generator.digits(start, end)
                        random.shuffle(Generator.password)
                        print("".join(Generator.password))
                    elif choice == 2:                        
                        Generator.chracters(start, end)
                        random.shuffle(Generator.password)
                        print("".join(Generator.password))
                    elif choice == 3:                        
                        Generator.specialChracters(start, end)
                        random.shuffle(Generator.password)
                        print("".join(Generator.password))
                    else:
                        print("Wrong choice.")
            else:
                print("Wrong choice.")
    
    def chracters(start : int = 5, end : int = 10) -> None:
        '''
        start and stop define range of chracters to be included.
        '''
        # string.ascii_letters: all upper and lower case letters
        for i in range(random.randint(start, end)):
            Generator.password.append(random.choice(list(string.ascii_letters)))
        
    def specialChracters(start : int = 5, end : int = 10) -> None:
        '''
        start and stop define range of special chracters to be included.
        '''
        special_characters = list("!@#$%^&*()-_=+[]}{|;:'\",.<>?/~`")
        for i in range(random.randint(start, end)):
            Generator.password.append(random.choice(special_characters))
    
    def digits(start : int = 5, end : int = 10) -> None:
        '''
        start and stop define range of digits to be included.
        '''
        digits = list("1234567890")
        for i in range(random.randint(start, end)):
            Generator.password.append(random.choice(digits))