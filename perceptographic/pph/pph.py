'''
Property-Preserving Hash parent class

Defines an interface than any PPH must implement

A PPH must implement 3 algorithms
    1) sample   : takes as input some security parameter, randomly generates a hash function
    2) hash     : takes as input some string x, returns h(x)
    3) evaluate : takes as input two hashes, returns whether they are similar or not
'''

import perceptographic.common as common
from abc import ABC, abstractmethod # abstract base class, a Python interface
import numpy as np


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
    
    @abstractmethod
    def save_description(self):
        pass
    
    @abstractmethod
    def load_from_description(self):
        pass
    
    # convert binary numpy array to hex string for clean output representation
    @staticmethod
    def to_hex(h):
        return common.np_binary_to_hex(h)

    # convert hex string to binary numpy array for internal use
    @staticmethod
    def to_np_binary(h):
        return common.hex_to_np_binary(h)
    