import re
import numpy as np

def predict_lr(model, images):
    preds  = np.squeeze(model.predict(images[:,:,::-1]))[:,:,::-1]
    preds += np.squeeze(model.predict(images))
    return preds/2

def str_extract(pattern, x):
    found = re.search(pattern, x)
    return found.group(1) if found else ''

def get_id(prefix=None):
    x = str(datetime.datetime.now())
    x = re.sub(" ", "_", x)
    x = re.sub(":", "-", x)
    x = x.split(".")[0]
    return f"{prefix}_{x}" if prefix else x

class ProgressLogger(object):
    
    def __init__(self):
        self.messages = []

    def append(self, line, level=0, verbose=True):
        line = '   '*level + line
        if verbose: print(line)
        self.messages.append(line)
        
    def display(self):
        for line in self.messages: print(line)
            
    def save(self, save_name):
        fwrite = open(save_name, "w") 
        for line in self.messages: fwrite.write(f"{line}\n") 
        fwrite.close()     
        
def save_log(save_name, progress_log):
    fwrite = open(save_name, "w") 
    for line in progress_log: 
        fwrite.write(f"{line}\n") 
    fwrite.close()     
