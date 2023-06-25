'''
This script loads the Tiny ImageNet dataset into memory
in an easy-to-use way. The result is 3 arrays:

category_ids : a 1-dimensional array of 200 IDs (nXXXXXXXX)

categories   : a 2-dimensional array with the (potentially
               multiple) names of each of the 200 categories,
               each categories[i] is a list of names

images       : a 2-dimensional array where each element
               images[i] contains an array of 500 image paths
               for category i

First things first, you should have the Tiny ImageNet dataset
downloaded and stored in a folder called dataset/ in the
project's root directory. You can download the dataset as follows.

cd <project root directory (where main.py is)>
mkdir dataset/
cd dataset/

wget http://cs231n.stanford.edu/tiny-imagenet-200.zip
unzip tiny-imagenet-200.zip
'''

import os
import subprocess

def load_dataset():
    folders = os.listdir('dataset/tiny-imagenet-200/train/')
    # the category id for a category is the name of the folder
    category_ids = folders

    category_name_file = open('dataset/tiny-imagenet-200/words.txt', 'r')
    lines = category_name_file.readlines()

    categories = []
    for folder in folders:
        for line in lines:
            if line.find(folder) >= 0:
                # drop the new line character
                line = line[:-1]
                # isolate the keywords which come after the tab,
                # then split by comma to get full keywords
                words = line.split('\t')[1].split(',')
                # eliminate leading whitespace
                words = [word.lstrip() for word in words]
                categories.append(words)

    images = []
    for folder in folders:
        folder_path = 'dataset/tiny-imagenet-200/train/' + folder + '/images/'
        image_paths = os.listdir(folder_path)
        images.append([(folder_path + path) for path in image_paths])

    return category_ids, categories, images
