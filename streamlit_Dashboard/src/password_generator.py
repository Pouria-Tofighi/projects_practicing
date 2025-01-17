import random 
import nltk
from abc import ABC,abstractmethod
import string

nltk.download('words')

class Password_generator(ABC):
    """
    This is the basic class which all classes must to derive from it
    """
    @abstractmethod
    def generate(self, ):
        '''
        Subclasses have to override this method
        '''
        pass

class RandomPasswordGenerator(Password_generator):
    def __init__(self, length: int = 8, number: bool = True, symble: str = True ):
        self.length = length
        self.charactors = string.ascii_letters
        if number:
            self.charactors += string.digits
        if symble:
            self.charactors += string.punctuation

    def generate(self):
        """
        This method returs a password
        """
        return "".join(random.choice(self.charactors) for _ in range(self.length))
    
class MemorablePasswordGenerator(Password_generator):
    def __init__(self, length: int = 5, capitalization = True, seperator = '-'):

        self.length = length
        self.capitalization = capitalization
        self.seperator = seperator
        self.vocabulary = nltk.corpus.words.words()


    def generate(self, ):
        password = [random.choice(self.vocabulary) for _ in range(self.length)]
        if self.capitalization:
            password = [words.upper() for words in password]

        return self.seperator.join(password)
    

class PinGenerator(Password_generator):
    def __init__(self, length: int = 4, Numbers = None):
        if Numbers is None:
            Numbers = string.digits
        self.length = length
        self.numbers = Numbers

    def generate(self, ):
        return ''.join(random.choice(self.numbers) for _ in range(self.length))
    