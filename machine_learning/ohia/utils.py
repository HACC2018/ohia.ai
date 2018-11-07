import os, re
import numpy as np
from PIL import Image

# create a directory if it doesn't already exist
def make_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def resize_smaller_dim(img, size=224):
    """ Resize the smaller dimension on an image
    
    Args:
        img: Input image opened from PIL  
        size: New size of the smaller dimension
        
    Returns: Resized image
    """
    w, h = img.size
    
    # width > height
    if w > h: 
        w = round(size*w/h)
        img = img.resize((w, size), resample=Image.LANCZOS)

    # height > width
    else: 
        h = round(size*h/w)
        img = img.resize((size, h), resample=Image.LANCZOS)
    
    return img

def crop_square(img, crop_type='center'):
    """ Crop larger dimension to produce a square image
    
    Args:
        img: Input image opened from PIL  
        crop_type: One of the following
            * if 'center' then take the center crop
            * if 'uniform' then take a uniform random crop
            * if 'triangular' then take a triangular random crop

    Returns: Cropped image
    """
    if isinstance(img, np.ndarray):
        h, w, _ = img.shape       
    else: 
        w, h = img.size
    
    crop_type_error = ValueError(
        'Undefinded crop_type parameter.'
        ' crop_type should be one of the following:'
        ' "center", "uniform", "triangular"'
    )
    
    if w > h: # width > height
        
        # get center
        if crop_type == 'center':
            c = w//2
        elif crop_type == 'uniform':
            c = round(w//2 + np.random.uniform(-1, 1) * (w-h)//2)
        elif crop_type == 'triangular':
            c = round(w//2 + np.random.triangular(-1, 0, 1) * (w-h)//2)
        else:
            raise crop_type_error
            
        # apply crop
        if isinstance(img, np.ndarray):
            img = img[:, c-h//2 : c+h//2]
        else:
            img = img.crop((c-h//2, 0, c+h//2, h))       
        
    else: # height > width
        
        # get center
        if crop_type == 'center':
            c = h//2
        elif crop_type == 'uniform':
            c = round(h//2 + np.random.uniform(-1, 1) * (h-w)//2)    
        elif crop_type == 'triangular':
            c = round(h//2 + np.random.triangular(-1, 0, 1) * (h-w)//2)    
        else:
            raise crop_type_error
            
        # apply crop
        if isinstance(img, np.ndarray):
            img = img[c-w//2 : c+w//2, :]
        else:
            img = img.crop((0, c-w//2, w, c+w//2))
                    
    return img