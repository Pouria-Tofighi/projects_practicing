"""
------------------------------------------------------This is a program which generate a password based on three methods.----------------------------------------------
"""
import string
import random
from abc import ABC, abstractmethod
import nltk

nltk.download("words")
print("\n")
#------------------------------------------------------------------------PASSWORD GENERATION--------------------------------------------------------------------------
class PasswordGenerator(ABC):
    """
    This class is considered as a based class
    """
    def generate(self, ):
        """
        Subclasses have to override this method to genereate a password. 
        """
        pass


class RandomPasswordGenerator(PasswordGenerator):
    """
    This class is able to generate a password based on the random alphabets, digits and symble.
    """
    def __init__(
            self,
            length: str = 8,
            include_numbers: bool = False,
            include_symbles: bool = False,
    ):
        self.character = string.ascii_letters
        self.length = length
        if include_numbers:
            self.character += string.digits
        if include_symbles:
            self.character += string.punctuation

    def generate(self, ):
        return "".join(random.choice(self.character) for _ in range(self.length))

 
class MemorablePasswordGenerator(PasswordGenerator):
    """
    This Class generates a password based on a list of vocabularies.
    If you do not identify a vocabulary, this class uses nltk library as its vocabulary
    """
    def __init__(
            self, 
            No_of_words: int = 5,
            seperator: str = '-',
            capitalization: bool = False,
            vocabulary: list = None
    ):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()

        self.No_of_words = No_of_words
        self.seperator = seperator
        self.capitalization = capitalization
        self.vocabulary = vocabulary

    def generate(self, ):
        """
        Generate a password from a list of vocabulary words.
        """
        password_word = [random.choice(self.vocabulary) for _ in range(self.No_of_words)]
        if self.capitalization:
            password_word = [word.upper() for word in password_word]
        return self.seperator.join(password_word)
    

class PinGenerator(PasswordGenerator):
    """
    This class generates a digit PIN Code.
    """
    def __init__(self, length: int = 4, ):
        self.length = length

    def generate(self, ) -> str:
        """
        Generate a numeric pin code.
        """

        return ''.join(random.choice(string.digits) for _ in range(self.length))
    

#------------------------------------------------------------------------CODE IMPLEMENTATION----------------------------------------------------------------------------
def main():
    while True:
        user_input = input("""Which kinds of password do you want (please enter its number):
                           \n1-Random Password
                           \n2-Memorable Password
                           \n3-PinCode
                           \nIf you want to exit, type 'q': """)
        print()
        
        if user_input.lower() == 'q':
            print("Closing the app...\nGoodBye")
            break
        if user_input == '1':
            #Check the lenght of the password
            while True:
                user_length = input("Enter the length of the password you want: ")
                if not user_length.isdigit():
                    print("Please enter a currect input")
                    print('\n')
                    continue
                else:
                    user_length = int(user_length)
                    print('\n')
                    break
            #Check if the password contains numbers    
            while True:
                include_num = input("Do you want to have numbers in your code (Y/N): ")
                print('\n')
                if include_num.lower() == 'y':
                    include_num = True
                    break
                elif include_num.lower() == 'n':
                    include_num = False
                    break
                else:
                    print("Please enter a currect format.")
                    print('\n')
                    continue
            #Check if the password contains symbles.
            while True:
                include_sym = input("Do you want to have punctuations in your code (Y/N): ")
                print('\n')
                if include_sym.lower() == 'y':
                    include_sym = True
                    break
                elif include_sym.lower() == 'n':
                    include_sym = False
                    break
                else:
                    print("please enter a currect format")
                    print('\n')
                    continue
            #Generate password
            random_pass = RandomPasswordGenerator(length=user_length, include_numbers=include_num, include_symbles=include_sym)
            password = random_pass.generate()
            print(f'Your password is:\n\n*** {password} ***\n')

            #Check if the user wants to restart the code.
            continue_generating = input("Do you want to generate another password (Y/N): ")
            if continue_generating.lower() == "y":
                continue
            else:
                break
        elif user_input == '2':
            while True:
                user_length = input("Enter the length of the password you want: ")
                if not user_length.isdigit():
                    print("Please enter a currect input")
                    print('\n')
                    continue
                else:
                    user_length = int(user_length)
                    print('\n')
                    break
            #Check if the user enters the seperator
            seperator = input("Which seperator do you consider of the code: ")
            print("\n")
            #Check if the user uses capital alphabets.
            while True:
                capital = input("Do you want use capital alphabets: (Y/N): ")
                print("\n")
                if capital.lower() == 'y':
                    capital = True
                    break
                elif capital.lower() == "n":
                    capital = False
                    break
                else:
                    print("Enter a currect format")
                    continue
            #Generate password
            random_pass = MemorablePasswordGenerator(No_of_words=user_length, seperator=seperator, capitalization=capital, )
            password = random_pass.generate()
            print (f'your password is:\n\n*** {password} ***\n')
            #Generate if the user wants to restart the code. 
            continue_generating = input("Do you want to generate another password (Y/N): ")
            print("\n")
            if continue_generating.lower() == "y":
                continue
            else:
                break
        elif user_input == '3':
            #check the lenght of the password
            while True:
                user_length = input("Enter the length of the password you want: ")
                if not user_length.isdigit():
                    print("Please enter a currect input")
                    print('\n')
                    continue
                else:
                    user_length = int(user_length)
                    print('\n')
                    break
            #Generate password
            random_pass = PinGenerator(length=user_length)
            password = random_pass.generate()
            print(f'Your password is\n\n*** {password} ***\n')
            #Check if the user wants to continue
            continue_generating = input("Do you want to generate another password (Y/N): ")
            if continue_generating.lower() == "y":
                continue
            else:
                break
        else:
            print("Please enter a currect input\n")
            continue

#------------------------------------------------------------------------CODE RUNNING----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
