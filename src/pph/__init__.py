from src.pph.pph import PPH
from src.pph.nonrobust import Nonrobust

__all__ = [
    'PPH',
    'Nonrobust'
]

# a function to create and return a property-preserving hash function
def create(algorithm='nonrobust', input_length=256, output_length=64):
    algorithm = algorithm.lower()
    match algorithm:
        case 'nonrobust':
            return Nonrobust(hash_length)
