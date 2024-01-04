'''
Perceptual Hash parent class

Defines an interface than any perceptual hash must implement

A perceptual hash must implement 2 algorithms
    1) hash     : takes as input some string x, returns h(x)
    2) evaluate : takes as input 2 hashes, returns value representing their similarity

Additionally, perceptual hashes must define their similarity metric as the
Hamming distance between hashes.

The Perceptual base class also has a static method to instantiate
a perceptual hash function. It takes as input a string representing
the perceptual hash algorithm and an integer hash length.
'''

from abc import ABC, abstractmethod # abstract base class, a Python interface


class Perceptual(ABC):

    @abstractmethod
    def hash(self, img):
        pass
    
    @abstractmethod
    def evaluate(self, h1, h2):
        pass
    
if __name__ == '__main__':
    phash = Perceptual.create('phash', 100)
    pdq = Perceptual.create('pdq', 100)
