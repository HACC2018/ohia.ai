import os, re, keras
import numpy as np
from PIL import Image
from skimage.exposure import adjust_gamma

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

class PlantNetGenerator(keras.utils.Sequence):
    
    def __init__(self,
                 file_list,
                 label_ids,
                 n_classes,
                 batch_size=32,
                 input_shape=(224, 224, 3),       
                 shuffle=True, 
                 augment=False):
        
        assert len(file_list) == len(label_ids)
        
        self.file_list = file_list
        self.label_ids = label_ids
        self.batch_size = batch_size
        self.input_shape = input_shape
        self.n_classes = n_classes
        self.shuffle = shuffle
        self.augment = augment
        self.on_epoch_end()

    def __len__(self):
        return int(np.floor(len(self.file_list) / self.batch_size))

    def __getitem__(self, index):
        
        # initialize values
        batch_inds = self.indexes[index*self.batch_size:(index+1)*self.batch_size]
        batch_files = [self.file_list[k] for k in batch_inds]
        X = np.empty((self.batch_size, *self.input_shape))
        y = self.label_ids[batch_inds]
        y = keras.utils.to_categorical(y, num_classes=self.n_classes)
        
        # Generate data
        if self.augment:
            for i, f in enumerate(batch_files):
                img = Image.open(f)
                img = crop_square(img, 'triangular')                       # random crop
                img = np.array(img, dtype=np.float)/255                    # convert to [0, 1] array
                img = adjust_gamma(img, np.random.triangular(0.5, 1, 2.5)) # brightness transformation
                if np.random.rand()>0.5: img = img[:,::-1,:]               # horizontal flip
                X[i] = 2*img - 1.0                                         # center pixel values
        else:
            for i, f in enumerate(batch_files):
                img = Image.open(f)
                img = crop_square(img)                  # center crop
                img = np.array(img, dtype=np.float)/255 # convert to [0, 1] array
                X[i] = 2*img - 1.0                      # center pixel values
        return X, y
    
    def on_epoch_end(self):
        self.indexes = np.arange(len(self.file_list))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)