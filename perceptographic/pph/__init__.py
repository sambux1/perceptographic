from perceptographic.pph.pph import PPH
from perceptographic.pph.nonrobust import Nonrobust
from perceptographic.pph.blv19 import BLV19
from perceptographic.pph.polynomial import Polynomial
from perceptographic.pph.hcrhf import HCRHF

__all__ = [
    'PPH',
    'Nonrobust',
    'BLV19',
    'Polynomial',
    'HCRHF'
]

# a function to create and return a property-preserving hash function
def create(algorithm='hcrhf', input_length=256, output_length=128, threshold=2):
    algorithm = algorithm.lower()
    match algorithm:
        case 'hcrhf':
            return HCRHF(input_length, output_length, threshold)
        case 'nonrobust':
            return Nonrobust(input_length, output_length, threshold)
