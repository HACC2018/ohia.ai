import click

FILE_PATH = '/home/matt/repos/ohia.ai/data'

def get_model(model_name, n_classes):

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

    # set freeze all layers
    for layer in base_model.layers:
        layer.trainable = False

    # map ImageNet features to plants
    x = base_model.output
    x = layers.GlobalAveragePooling2D()(x)
    outputs = layers.Dense(n_classes, activation='softmax')(x)

    # compile the model
    model = Model(inputs=base_model.input, outputs=outputs)
    model.compile(
        optimizer=Adam(lr=0.001),
        loss='categorical_crossentropy',
        metrics=[top_1_accuracy, top_3_accuracy, top_5_accuracy]
    )

    return model

@click.command()
@click.option('--model_name', help='Name of neural network architecture, one of "mobilenetv1", "mobilenetv2", "nasnetmobile"', required=True)
@click.option('--seed', default=1, help='Random seed.')
@click.option('--batch_size', default=32, help='Number of observations needed before updating weights.')
@click.option('--filtered', default=False, help='Boolean flag.  If true then use filtered images.')
@click.option('--augmentation', default=False, help='Boolean flag.  If true then perform data augmentation.')
@click.option('--n_thread', default=1, help='Number of threads to use.')
@click.option('--gpu', default=0, help='Id of gpu to use.')
@click.option('--save_model', default=False, help='Boolean flag.  If true then save the model in a tfjs format.')


def main(model_name, seed, batch_size, filtered, augmentation, n_thread, gpu, save_model):

    
    import os, re, glob, json
    os.environ['CUDA_DEVICE_ORDER']='PCI_BUS_ID'
    os.environ['CUDA_VISIBLE_DEVICES']=str(gpu)

    import numpy as np
    import pandas as pd

    from keras import callbacks
    from sklearn.model_selection import train_test_split

    from ohia.encoders import FastLabelEncoder
    from ohia.utils import PlantNetGenerator, make_dir

    # set up paths
    IMAGE_DIR = ('filtered_' if filtered else '') + 'images_preprocessed'
    model_path = (
        f'{FILE_PATH}/models/{model_name}' +
        f'_seed-{seed}' +
        f'_batch_size-{batch_size}' +
        ('_filtered' if filtered else '') +
        ('_augmentation' if augmentation else '')
    )
    print(model_path)
    make_dir(model_path)

    # get list of images and labels
    file_list = glob.glob(f'{FILE_PATH}/{IMAGE_DIR}/**/*.jpg', recursive=True)
    full_label_list = [re.split('/', f)[-2] for f in file_list]

    # encode label names with ids
    fle = FastLabelEncoder()
    label_ids = fle.fit_transform(full_label_list)

    # save id2label map
    id2label = {int(fle.transform([label])):label for label in np.unique(full_label_list)}
    with open(f'{model_path}/plantnet_classes.json', 'w') as fp:
        json.dump(id2label, fp)

    # split data
    train_files, valid_files, train_ids, valid_ids \
        = train_test_split(file_list, label_ids, test_size=0.1, random_state=seed)

    # create generators
    n_classes = len(np.unique(full_label_list))
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
    model = get_model(model_name, n_classes)
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
        model = get_model(model_name, n_classes)
        best_weights = glob.glob(f'{model_path}/**.h5')
        best_weights = np.sort(best_weights)[-1]
        model.load_weights(best_weights)
        tfjs.converters.save_keras_model(model, f'{model_path}//{model_name}')


if __name__ == '__main__':
    """
    python finetune.py \
      --model_name mobilenetv1 \
      --filtered True \
      --augmentation True \
      --n_thread 8 \
      --gpu 1 \
    """
    main()