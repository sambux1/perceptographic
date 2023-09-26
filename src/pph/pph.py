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
    def hash(h, x):
        pass
    
    @abstractmethod
    def evaluate(h, y1, y2):
        pass
    