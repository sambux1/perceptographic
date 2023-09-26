'''
An implementation of the PPH described in section 6 of the following paper
by Holmgren et. al.

https://eprint.iacr.org/2022/842.pdf
'''

from pph import PPH


class HLTW22(PPH):
    
    def __init__(self):
        print('hey there')
    
    def sample(parameter):
        return 0
    
    def hash(h, x):
        # check hash is callable
        return h(x)
    
    def evaluate(h, y1, y2):
        return y1 == y2
