import re
import numpy as np
from PIL import Image

def predict_lr(model, images):
    preds  = np.squeeze(model.predict(images[:,:,::-1]))[:,:,::-1]
    preds += np.squeeze(model.predict(images))
    return preds/2

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


def crop_square(img):
    """ Crop larger dimension to produce a square image
    
    Args:
        img: Input image opened from PIL  

    Returns: Cropped image
    """
    w, h = img.size
        
    # width > height
    if w > h: 
        c = round(w//2 + np.random.uniform(-1, 1, 1)[0] * (w-h)//2)
        img = img.crop((c-h//2, 0, c+h//2, h))
        
    # height > width
    else:
        c = round(h//2 + np.random.uniform(-1, 1, 1)[0] * (h-w)//2)    
        img = img.crop((0, c-w//2, w, c+w//2))
        
    return img