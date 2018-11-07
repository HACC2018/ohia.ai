import click

FILE_PATH = '/home/matt/repos/ohia.ai/data'

def get_model_path(model_name, training_type, seed, batch_size, augmentation):
    """ Get path for given model parameters
    
    Args:
        model_name: Name of neural network architecture, one of
          "mobilenetv1", "mobilenetv2", "nasnetmobile"
        training_type: Integer encoding:
            * if 0 fine-tune
            * if 1 pretrain
            * if 2 load pretrained then fine-tune.
        seed: Random seed.
        batch_size: Number of observations needed before updating weights.
        augmentation: Boolean flag.  If true then perform data augmentation.
    """
    model_path = f'{FILE_PATH}/models/'
    
    # fine-tuning
    if training_type == 0:
        model_path += f'finetuned_{model_name}'
        model_path += '_with_augmention' if augmentation else ''
        
    # pretraining
    elif training_type == 1:
        model_path += f'pretrained_{model_name}'
        model_path += '_with_augmention' if augmentation else ''
        
    # pretraining then fine-tuning
    elif training_type == 2:
        model_path += f'finetuned_{model_name}'
        model_path += '_with_augmention' if augmentation else ''
        model_path += '_using_plantnet_pretrained'
    else :
        raise ValueError('training_type must be either 0, 1, or 2.') 
            
    model_path += f'_seed-{seed}_batch_size-{batch_size}'
    return model_path

def get_model(model_name, n_classes, training_type, pretrain_file=None):
    """ Get ohiaNet architecture
    
    Args:
        model_name: Name of neural network architecture, one of
          "mobilenetv1", "mobilenetv2", "nasnetmobile"
        n_classes: Numeber of output units
        training_type: Integer encoding:
            * if 0 fine-tune
            * if 1 pretrain
            * if 2 load pretrained then fine-tune.
            
    Returns: Keras model.
    """        
    from keras import layers, Model
    from keras.optimizers import Adam
    from keras.applications.mobilenet import MobileNet
    from keras.applications.mobilenetv2 import MobileNetV2
    from keras.applications.nasnet import NASNetMobile
    from ohia.metrics import top_1_accuracy, top_3_accuracy, top_5_accuracy

    import keras.backend as K
    K.clear_session()

    # load pretrained ImageNet model
    if model_name == 'mobilenetv1':
        base_model = MobileNet(
            input_shape=(224,224,3),
            weights='imagenet',
            include_top=False
        )        
    elif model_name == 'mobilenetv2':
        base_model = MobileNetV2(
            input_shape=(224,224,3),
            alpha=1.4,
            weights='imagenet',
            include_top=False
        )
    elif model_name == 'nasnetmobile':
        base_model = NASNetMobile(
            input_shape=(224,224,3),
            weights='imagenet',
            include_top=False
        )
    else:
        assert ValueError(
            f'model_name parameter must be one of the following'
            ' "mobilenetv1",'
            ' "mobilenetv2",'
            ' "nasnetmobile"'
        )

        
    if training_type==0:
        
        # map ImageNet features to plants
        x = base_model.output
        x = layers.GlobalAveragePooling2D()(x)
        outputs = layers.Dense(n_classes, activation='softmax')(x)
        model = Model(inputs=base_model.input, outputs=outputs)        
        
        # freeze all but the last layer
        for layer in model.layers[:-1]:
            layer.trainable = False

    elif training_type==1:
        
        # map ImageNet features to plants
        x = base_model.output
        x = layers.GlobalAveragePooling2D()(x)
        outputs = layers.Dense(n_classes, activation='softmax')(x)
        model = Model(inputs=base_model.input, outputs=outputs)        
                    
    elif training_type==2:
        
        N_PLANTNET_CLASSES = 436
            
        # map ImageNet features to plants
        x = base_model.output
        x = layers.GlobalAveragePooling2D()(x)
        outputs = layers.Dense(N_PLANTNET_CLASSES, activation='relu')(x)

        # load the model
        pretrained_model = Model(inputs=base_model.input, outputs=outputs)
        pretrained_model.load_weights(pretrain_file)
        
        # add final layer
        outputs = layers.Dense(n_classes, activation='softmax')(pretrained_model.output)
        model = Model(inputs=pretrained_model.input, outputs=outputs)

        # freeze all but the last two layers
        if training_dataset == 'scraped':
            for layer in model.layers[:-2]:
                layer.trainable = False
            
    else :
        raise ValueError('training_type must be either 0, 1, or 2.') 
                
    # compile the model
    model.compile(
        optimizer=Adam(lr=0.001),
        loss='categorical_crossentropy',
        metrics=[top_1_accuracy, top_3_accuracy, top_5_accuracy]
    )

    return model


@click.command()
@click.option('--model_name', help='Name of neural network architecture, one of "mobilenetv1", "mobilenetv2", "nasnetmobile"', required=True)
@click.option('--training_type', default=0, help='Integer encoding: 0=fine-tune, 1=pretrain, 2=load pretrained then fine-tune')

@click.option('--seed', default=1, help='Random seed.')
@click.option('--batch_size', default=32, help='Number of observations needed before updating weights.')
@click.option('--augmentation', default=False, help='If true then perform data augmentation.')

@click.option('--gpu', default=0, help='Id of gpu to use.')
@click.option('--n_thread', default=1, help='Number of threads to use.')
@click.option('--save_model', default=False, help='If true then save the model in a tfjs format.')


def main(model_name, training_type, seed, batch_size, augmentation, n_thread, gpu, save_model):

    
    import os, re, glob, json
    os.environ['CUDA_DEVICE_ORDER']='PCI_BUS_ID'
    os.environ['CUDA_VISIBLE_DEVICES']=str(gpu)

    import numpy as np
    import pandas as pd

    from keras import callbacks
    from sklearn.model_selection import train_test_split

    from ohia.generators import PlantNetGenerator
    from ohia.encoders import FastLabelEncoder
    from ohia.utils import make_dir

    # make directory for current experiment
    model_path = get_model_path(model_name, 1, seed, batch_size, augmentation)
    make_dir(model_path)

    # get pretrained file
    if training_type == 2:
        pretrain_path = get_model_path(model_name, 1, seed, batch_size, False)
        pretrain_file = np.sort(glob.glob(f'{pretrain_path}/**.h5'))[-1]
    else:
        pretrain_file = None

    # get list of images and labels
    image_dir = 'plantnet_filtered'if training_type==1 else 'scraped_filtered'
    file_list = glob.glob(f'{FILE_PATH}/preprocessed_images/{image_dir}/**/*.jpg', recursive=True)
    label_list = [re.split('/', f)[-2] for f in file_list]

    # encode label names with ids
    fle = FastLabelEncoder()
    label_ids = fle.fit_transform(label_list)

    # save id2label map
    id2label = {int(fle.transform([label])):label for label in np.unique(label_list)}
    with open(f'{model_path}/plantnet_classes.json', 'w') as fp:
        json.dump(id2label, fp)

    # split data
    train_files, valid_files, train_ids, valid_ids \
        = train_test_split(file_list, label_ids, test_size=0.1, random_state=seed)

    # create generators
    n_classes = len(np.unique(label_list))
    train_generator = PlantNetGenerator(
        train_files, train_ids, n_classes,
        batch_size=batch_size,
        augment=augmentation
    )
    valid_generator = PlantNetGenerator(
        valid_files, valid_ids, n_classes,
        batch_size=batch_size,
        augment=augmentation,
        shuffle=False
    )

    # define callbacks
    callbacks_list = [
        callbacks.EarlyStopping(
            monitor='val_top_3_accuracy',
            patience=10,
            verbose=1,
            mode='max',
        ),
        callbacks.ReduceLROnPlateau(
            monitor='val_top_3_accuracy',
            factor=0.25,
            patience=2,
            verbose=1,
            mode='max',
        ),
        callbacks.ModelCheckpoint(
            monitor='val_top_3_accuracy',
            filepath=f'{model_path}/weights' + '_{epoch:02d}.h5',
            save_best_only=True,
            save_weights_only=False,
            mode='max',
        ),
    ]

    # train model 
    model = get_model(model_name, n_classes, training_type, pretrain_file)
    model.fit_generator(
        generator=train_generator,
        validation_data=valid_generator,
        callbacks=callbacks_list,
        use_multiprocessing=True,
        workers=n_thread,
        epochs=100,    
    )

    # save results
    results = pd.DataFrame(model.history.history)
    results.to_csv(f'{model_path}/results.csv', index=False)

    # print best results
    print(results.iloc[results.val_top_3_accuracy.values.argmax()])

    # save best model
    if save_model:
        import tensorflowjs as tfjs
        model = get_model(model_name, n_classes, training_type, pretrain_file)
        best_weights = glob.glob(f'{model_path}/**.h5')
        best_weights = np.sort(best_weights)[-1]
        model.load_weights(best_weights)
        tfjs.converters.save_keras_model(model, f'{model_path}/{model_name}')


if __name__ == '__main__':
    """
    python train.py \
      --model_name mobilenetv1 \
      --training_type 0 \
      --augmentation True \
      --n_thread 8 \
      --gpu 1 \
    """
    main()