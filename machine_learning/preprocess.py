import os, re, multiprocessing
import numpy as np
from PIL import Image
from ohia.utils import resize_smaller_dim, crop_square

IMAGE_PATH = '/home/matt/repos/ohia.ai/data'
INPUT_DIR  = 'images'
OUTPUT_DIR = 'preprocessed_images'

# create wrapper to parallelize
def resize_crop_and_save(f):
    try:
        img = Image.open(f)
        img = resize_smaller_dim(img)
        img = crop_square(img)
        img.save(re.sub(INPUT_DIR, OUTPUT_DIR, f))
        return(1)
    except:
        return(0)
    
if __name__ == '__main__':

    # create directory
    if not os.path.exists(f'{IMAGE_PATH}/{OUTPUT_DIR}'):
        os.makedirs(f'{IMAGE_PATH}/{OUTPUT_DIR}')

    # create subdirectories
    dir_list = os.listdir(f'{IMAGE_PATH}/{INPUT_DIR}')
    for d in dir_list:
        dname = f'{IMAGE_PATH}/{OUTPUT_DIR}/{d}'
        if not os.path.exists(dname):
            os.makedirs(dname)

    # get list of images
    file_list = [os.path.join(dp, f) 
                 for dp, dn, fnames in os.walk(f'{IMAGE_PATH}/{INPUT_DIR}')
                 for f in fnames if os.path.splitext(f)[1]=='.jpg']        

    # resize and save (in parallel)
    pool = multiprocessing.Pool(10)
    successes = pool.map(resize_crop_and_save, file_list)
    pool.close()

    print(f'{np.sum(successes)} resized ({100*np.mean(successes)}%)')
