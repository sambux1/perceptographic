'''
Property-Preserving Hash parent class

Defines an interface than any PPH must implement

A PPH must implement 3 algorithms
    1) sample   : takes as input some security parameter, randomly generates a hash function
    2) hash     : takes as input some string x, returns h(x)
    3) evaluate : takes as input two hashes, returns whether they are similar or not
'''

from abc import ABC, abstractmethod # abstract base class, a Python interface


class PPH(ABC):

    @abstractmethod
    def sample(parameter):
        pass
    
    @abstractmethod
    def hash(self, x):
        pass
    
    @abstractmethod
    def evaluate(self, y1, y2):
        pass
    
    # convert binary numpy array to hex string for clean output representation
    @staticmethod
    def to_hex(h):
        str_repr = ''
        for bit in h:
            str_repr += str(bit)
        return hex(int(str_repr, 2))[2:]