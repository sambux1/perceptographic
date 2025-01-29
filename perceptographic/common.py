# a file for general purpose functions that are useful for many constructions
import numpy as np


'''
Conversions
'''
def np_binary_to_hex(x):
    return np.packbits(x).tobytes().hex()

def hex_to_np_binary(x):
    return np.unpackbits(np.frombuffer(bytes.fromhex(x), dtype=np.uint8))
