'''
Perceptual Hash parent class

Defines an interface than any perceptual hash must implement

A perceptual hash must implement 2 algorithms
    1) hash     : takes as input some string x, returns h(x)
    2) evaluate : takes as input 2 hashes, returns value representing their similarity

Additionally, perceptual hashes must define their similarity metric as the
Hamming distance between hashes.
'''

from abc import ABC, abstractmethod # abstract base class, a Python interface


class Perceptual(ABC):

    @abstractmethod
    def hash(self, img):
        pass
    
    @abstractmethod
    def evaluate(self, h1, h2):
        pass