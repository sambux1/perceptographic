from perceptographic.perceptual.perceptual import Perceptual
from perceptographic.perceptual.image import Image
from perceptographic.perceptual.phash import PHash
from perceptographic.perceptual.pdq import PDQ

__all__ = [
    'Perceptual',
    'PHash',
    'PDQ',
    'Image',
    'create'
]

# a function to create and return a perceptual hash function
def create(algorithm='phash', hash_length=256):
    algorithm = algorithm.lower()
    match algorithm:
        case 'phash':
            return PHash(hash_length)
        case 'pdq':
            return PDQ(hash_length)
