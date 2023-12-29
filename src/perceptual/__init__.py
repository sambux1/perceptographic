from src.perceptual.perceptual import Perceptual
from src.perceptual.image import Image
from src.perceptual.phash import PHash
from src.perceptual.pdq import PDQ

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
