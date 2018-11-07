import os, re, glob, multiprocessing, click
import numpy as np
from PIL import Image
from collections import Counter
from ohia.utils import resize_smaller_dim, crop_square, make_dir
from functools import partial


# create wrapper to parallelize
def resize_crop_and_save(f, input_dir, output_dir, crop):
    try:
        img = Image.open(f)
        if img.mode == 'RGB':
            img = resize_smaller_dim(img)
            if crop:
                img = crop_square(img, 'center')
            img.save(re.sub(input_dir, output_dir, f))
            return(1)
        else:
            print(f'Skipping {f}')
            return(0)
        
    except:
        print(f'Skipping {f}')
        return(0)
    


@click.command()
@click.option('--input_dir', help='Input directory of images.', required=True)
@click.option('--output_dir', help='Output directory of images.', required=True)
@click.option('--file_path', default='/home/matt/repos/ohia.ai/data', help='Absolute path to data directories.')
@click.option('--min_count', default=1, help='Minimum numbers of images needed to create a class.')
@click.option('--n_thread', default=1, help='Number of threads to use.')
@click.option('--crop', default=False, help='Either: "center", "triangular" or "uniform".')
def main(input_dir, output_dir, min_count, n_thread, crop):

    # get list of images
    file_list = glob.glob(f'{file_path}/{input_dir}/**/*.jpg', recursive=True)
        
    # filter images
    label_list = [re.split('/', f)[-2] for f in file_list]
    label_counts = Counter(label_list)
    filtered_labels = [k for k,v in label_counts.items() if v>min_count]
    filtered_file_list = [f for f,n in zip(file_list, label_list) if n in filtered_labels]

    # create subdirectories
    make_dir(f'{file_path}/{output_dir}')
    for dir_name in filtered_labels:
        make_dir(f'{file_path}/{output_dir}/{dir_name}')

    # resize and save (in parallel)
    pool = multiprocessing.Pool(n_thread)
    f = partial(resize_crop_and_save, input_dir=input_dir, output_dir=output_dir, crop=crop)
    successes = pool.map(f, filtered_file_list)
    pool.close()

    print(f'{np.sum(successes)} resized ({100*np.mean(successes)}%)')

if __name__ == '__main__':
    """
    python preprocess.py \
      --input_dir raw_images \
      --output_dir filtered_images
    """
    main()