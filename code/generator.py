'''
All the functionality for generating random passwords.
'''

import random
import string

class Generator:
    password = []
    
    def runner() -> None:
        '''
        Runs the whole password generator functionality.
        '''
        while True:
            print("Enter 0 to exit: ")
            print("Enter 1 to generate fully random password: ")
            print("Enter 2 to customize it: ")
            choice = int(input("Enter: "))
            if choice == 0:
                break
            elif choice == 1:
                remove = int(input("0 to clear buffer or 1 to keep extending size: "))
                if remove == 0: Generator.password.clear()
                
                Generator.chracters()
                Generator.specialChracters()
                Generator.digits()
                random.shuffle(Generator.password)
                print("------------------------------")
                print(f"Fully random password: {"".join(Generator.password)}")
                print("------------------------------")
            elif choice == 2:
                while True:
                    choice = int(input("Enter 0 to exit: \nEnter 1 to add digits: \nEnter 2 to add letters: \nEnter 3 to add special chracters: \nEnter: "))
                    
                    remove = int(input("Enter 0 to clear buffer and 1 to keep adding to it: "))    
                    if remove == 0: Generator.password.clear()
                    
                    if choice == 0:
                        break
                    elif choice == 1:
                        start = int(input("Enter what should be minimum number of digits in the password: "))
                        end = int(input("Enter what should be maximum number of digits in the password: "))
                        Generator.digits(start, end)
                        print("".join(Generator.password))
                    elif choice == 2:
                        start = int(input("Enter what should be minimum number of letters in the password: "))
                        end = int(input("Enter what should be maximum number of letters in the password: "))
                        Generator.chracters(start, end)
                        print("".join(Generator.password))
                    elif choice == 3:
                        start = int(input("Enter what should be minimum number of special chracters in the password: "))
                        end = int(input("Enter what should be maximum number of special chracters in the password: "))
                        Generator.specialChracters(start, end)
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
        
    def specialChracters(start : int = 5, end : int = 10) -> None:
        '''
        start and stop define range of special chracters to be included.
        '''
        special_characters = list("!@#$%^&*()-_=+[]}{|;:'\",.<>?/~`")
        for i in range(random.randint(start, end)):
            random.shuffle(Generator.password.append(random.choice(special_characters)))
    
    def digits(start : int = 5, end : int = 10) -> None:
        '''
        start and stop define range of digits to be included.
        '''
        digits = list("1234567890")
        for i in range(random.randint(start, end)):
            random.shuffle(Generator.password.append(random.choice(digits)))