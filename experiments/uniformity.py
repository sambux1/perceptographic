# this is necessary (temporarily) to be able to import the library
import sys
sys.path.insert(1, "../")

from load_tinyimagenet import load_dataset
import perceptographic

category_ids, categories, images = load_dataset()


# function to evaluate a given perceptual/perceptographic hash function's
#  output uniformity on the dataset
def test_uniformity(hash_function):
    # do the stuff here
    # for each image, run the hash function, store results somehow
    # see what overall average output is / what the average similarity is
    # see if image categories have skewed averages / more than random similarity

    # each perceptual/perceptographic hash function supports the hash() function on
    #  an image object
    pass