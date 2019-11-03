from keras.applications.vgg16 import VGG16
from keras.models import Model
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator


# A function that defines a neural network model and returns its ready-to-learn form
def define_model():
    # loading the VGG16 model
    model = VGG16(include_top=False, input_shape=(224, 224, 3))
    # marking loaded layers as not trainable
    for layer in model.layers:
        layer.trainable = False
    # adding new classifier layers
    flat1 = Flatten()(model.layers[- 1].output)
    class1 = Dense(128, activation='relu', kernel_initializer='he_uniform')(flat1)
    output = Dense(1, activation='sigmoid')(class1)
    # defining a new model
    model = Model(inputs=model.inputs, outputs=output)
    # compiling the model
    opt = SGD(lr=0.001, momentum=0.9)
    model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
    return model


# A function that starts the learning process of the neural network model and returns its learned form
def run_training():
    model = define_model()
    # creating a data generator
    datagen = ImageDataGenerator(featurewise_center=True)
    # specifying imagenet mean values for centering
    datagen.mean = [123.68, 116.779, 103.939]
    # preparing an iterator
    train_it = datagen.flow_from_directory('training_dataset/',
                                           class_mode='binary', batch_size=64, target_size=(224, 224))
    # model fitting
    model.fit_generator(train_it, steps_per_epoch=len(train_it), epochs=5, verbose=0)
    # saving the model
    model.save('dogs_and_cats_model.h5')


# entry point to start learning
run_training()
