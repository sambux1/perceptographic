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
    def get_hash_length(self):
        pass

    @abstractmethod
    def hash(self, img):
        pass
    
    @abstractmethod
    def evaluate(self, h1, h2):
        pass
    
    # we need the output of a perceptual hash function to be a binary numpy array
    # the default implementation works on hex strings
    # it can be overridden if the hashes are of a different type
    @staticmethod
    def to_np_binary(h1):
        #TODO: implement a default function when hash is hex string
        pass
    
if __name__ == '__main__':
    phash = Perceptual.create('phash', 100)
    pdq = Perceptual.create('pdq', 100)
