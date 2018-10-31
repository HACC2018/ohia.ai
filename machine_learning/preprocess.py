import os, re, multiprocessing
import numpy as np
from PIL import Image
from ohia.utils import resize_smaller_dim

IMAGE_PATH = '/home/matt/repos/ohia.ai/data/images'

# create wrapper to parallelize
def resize_and_save(f):
    try:
        img = Image.open(f)
        img = resize_smaller_dim(img)
        img.save(re.sub('images', 'resized_images', f))
        return(1)
    except:
        return(0)

if __name__ == '__main__':

    # get list of images
    file_list = [os.path.join(dp, f) for dp, dn, fnames in os.walk(IMAGE_PATH) for f in fnames if os.path.splitext(f)[1]=='.jpg']        

    # resize and save (in parallel)
    pool = multiprocessing.Pool(10)
    successes = pool.map(resize_and_save, file_list)
    pool.close()

    print(f'{np.sum(successes)} resized ({100*np.mean(successes)}%)')