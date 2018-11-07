"""
File: generators.py
Author: Team ohia.ai
Description: A custom generator created for the HAAC 2018 Challenge.
"""

import keras
import numpy as np
from PIL import Image
from skimage.exposure import adjust_gamma
from ohia.utils import crop_square, resize_smaller_dim

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