from perceptographic.pph.pph import PPH
from perceptographic.pph.nonrobust import Nonrobust
from perceptographic.pph.blv19 import BLV19

__all__ = [
    'PPH',
    'Nonrobust',
    'BLV19'
]

# a function to create and return a property-preserving hash function
def create(algorithm='nonrobust', input_length=256, output_length=64, threshold=100):
    algorithm = algorithm.lower()
    match algorithm:
        case 'nonrobust':
            return Nonrobust(input_length, output_length, threshold)
