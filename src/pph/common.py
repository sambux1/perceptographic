'''
A file of common functions that are relevant for many constructions.
'''

import math

# input  : array of base n values
# outout : hex string
def base_n_to_hex(x, base):
    # calculate the width of the output value

    num_hex_symbols = math.ceil(len(x) / math.log(16, base))
    base_n = 0
    for val in x:
        base_n *= base
        base_n += val

    # pad the output to the fixed width calculated above
    return '0x' + hex(base_n)[2:].zfill(num_hex_symbols)

# input  : hex string
# outout : array of base n values
def hex_to_base_n(x, base):
    return numberToBase(int(x, 16), base)

#TODO: clean this up
def numberToBase(x, b):
    if x == 0:
        return [0]
    digits = []
    while x:
        digits.append(int(x % b))
        x //= b
    return digits[::-1]