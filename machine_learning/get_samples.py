"""
File: get_samples.py
Author: Matt Motoki
Description: Creates a directory for each plant containing a small sample of images.
"""

import re, glob
import numpy as np
from PIL import Image
from ohia.utils import make_dir

FILE_PATH = '/home/matt/repos/ohia.ai/data'
IMAGE_DIR = 'preprocessed_images/scraped_filtered'


# get list of images and labels
file_list = glob.glob(f'{FILE_PATH}/images/**/*.jpg', recursive=True)
label_list = [re.split('/', f)[-2] for f in file_list]

make_dir(f'{FILE_PATH}/sample_images')
for lookup in np.unique(label_list):
    make_dir(f'{FILE_PATH}/sample_images/{lookup}')
    
    count = 0
    for f,n in zip(file_list, label_list):
        if count==5:
            break
        if lookup==n:
            try:
                img = Image.open(f)
                img.save(re.sub('images', 'sample_images', f))
                count += 1
            except:
                print(f'Skipping {f}')