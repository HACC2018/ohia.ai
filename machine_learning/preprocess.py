import os, re, glob, multiprocessing
import numpy as np
from PIL import Image
from collections import Counter
from ohia.utils import resize_smaller_dim, crop_square

MIN_COUNT = 100
FILE_PATH = '/home/matt/repos/ohia.ai/data'
INPUT_DIR = 'images'
OUTPUT_DIR = 'preprocessed_images' # 'resized_images'

# create wrapper to parallelize
def resize_crop_and_save(f):
    try:
        img = Image.open(f)
        if img.mode == 'RGB':
            img = resize_smaller_dim(img)
            img = crop_square(img)
            img.save(re.sub(INPUT_DIR, OUTPUT_DIR, f))
            return(1)
        else:
            print(f'Skipping {f}')
            return(0)
        
    except:
        print(f'Skipping {f}')
        return(0)
    
# create a directory if it doesn't already exist
def make_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

if __name__ == '__main__':

    # get list of images
    file_list = glob.glob(f'{FILE_PATH}/{INPUT_DIR}/**/*.jpg', recursive=True)
        
    # filter images
    label_list = [re.split('/', f)[-2] for f in file_list]
    label_counts = Counter(label_list)
    filtered_labels = [k for k,v in label_counts.items() if v>MIN_COUNT]
    filtered_file_list = [f for f,n in zip(file_list, label_list) if n in filtered_labels]

    # create subdirectories
    make_dir(f'{FILE_PATH}/{OUTPUT_DIR}')
    for dir_name in filtered_labels:
        make_dir(f'{FILE_PATH}/{OUTPUT_DIR}/{dir_name}')

    # resize and save (in parallel)
    pool = multiprocessing.Pool(10)
    successes = pool.map(resize_crop_and_save, filtered_file_list)
    pool.close()

    print(f'{np.sum(successes)} resized ({100*np.mean(successes)}%)')
