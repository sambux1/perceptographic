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
import numpy as np


class Perceptual(ABC):

    @abstractmethod
    def get_hash_length(self):
        pass

    # hashes can either be binary numpy arrays (if used as part of a perceptographic construction) 
    #   or hex strings (if used as a standalone function)
    @abstractmethod
    def hash(self, img, as_hex=False):
        pass
    
    # evaluation should return an integer representing Hamming distance
    @abstractmethod
    def evaluate(self, h1, h2, as_hex=False):
        pass
    
    # convert binary numpy array to hex string for clean output representation
    @staticmethod
    def to_hex(h):
        return np.packbits(h).tobytes().hex()
    
    # we need the output of a perceptual hash function to be a binary numpy array
    # the default implementation works on hex strings
    # it can be overridden if the hashes are of a different type
    @staticmethod
    def to_np_binary(h):
        return np.unpackbits(np.frombuffer(bytes.fromhex(h), dtype=np.uint8))
