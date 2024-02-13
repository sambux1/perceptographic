# this is necessary (temporarily) to be able to import the library
import sys
import time
sys.path.insert(1, "../")

from load_tinyimagenet import load_dataset
import perceptographic

category_ids, categories, images = load_dataset()


def normalize_hex(hex_value):
    max_value = int('F' * len(hex_value), 16)
    value = int(hex_value, 16)
    normalized = value / max_value
    return normalized

# function to evaluate a given perceptual/perceptographic hash function's
#  output uniformity on the dataset
def test_uniformity(hash_function):
    results = {}
    for i in range(len(category_ids)):
        sum_normalized = 0
        max_normalized = 0
        min_normalized = 1
        for image_filename in images[i]:
            img = perceptographic.perceptual.Image(image_filename)
            h = hash_function.hash(img)
            normalized = normalize_hex(str(h))
            
            sum_normalized += normalized
            max_normalized = max(max_normalized, normalized)
            min_normalized = min(max_normalized, normalized)
        
        sum_normalized /= len(images[i])
        results[category_ids[i]] = (sum_normalized, max_normalized, min_normalized)
    
    return results


perceptual = perceptographic.perceptual.PHash(256)
results1 = test_uniformity(perceptual)
max_avg = 0
min_avg = 1
max_max = 0
min_max = 1
max_min = 0
min_min = 1
for i in range(len(results1)):
    max_avg = max(max_avg, results1[category_ids[i]][0])
    min_avg = min(min_avg, results1[category_ids[i]][0]) 
    max_max = max(max_max, results1[category_ids[i]][1])
    min_max = min(min_max, results1[category_ids[i]][1]) 
    max_min = max(max_min, results1[category_ids[i]][2])
    min_min = min(min_min, results1[category_ids[i]][2])
print('Avg: ', min_avg, '-', max_avg)
print('Max: ', min_max, '-', max_max)
print('Min: ', min_min, '-', max_min)

nonrobust = perceptographic.Perceptographic('phash', 'nonrobust', 1600, 200, 256)
results2 = test_uniformity(nonrobust)
max_avg = 0
min_avg = 1
max_max = 0
min_max = 1
max_min = 0
min_min = 1
for i in range(len(results2)):
    max_avg = max(max_avg, results2[category_ids[i]][0])
    min_avg = min(min_avg, results2[category_ids[i]][0]) 
    max_max = max(max_max, results2[category_ids[i]][1])
    min_max = min(min_max, results2[category_ids[i]][1]) 
    max_min = max(max_min, results2[category_ids[i]][2])
    min_min = min(min_min, results2[category_ids[i]][2])
print('Avg: ', min_avg, '-', max_avg)
print('Max: ', min_max, '-', max_max)
print('Min: ', min_min, '-', max_min)