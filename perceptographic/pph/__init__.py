from perceptographic.pph.pph import PPH
from perceptographic.pph.nonrobust import Nonrobust
from perceptographic.pph.log_threshold import LogThreshold

__all__ = [
    'PPH',
    'Nonrobust',
    'LogThreshold'
]

# a function to create and return a property-preserving hash function
def create(algorithm='log_threshold', input_length=1024, output_length=128, threshold=2):
    algorithm = algorithm.lower()
    match algorithm:
        case 'log_threshold':
            return LogThreshold(input_length, threshold)
        case 'nonrobust':
            return Nonrobust(input_length, output_length, threshold)
