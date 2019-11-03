from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model


# A function that loads an image and transforms it into the appropriate form
def load_image(filename):
    img = load_img(filename, target_size=(224, 224))
    img = img_to_array(img)
    img = img.reshape(1, 224, 224, 3)
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    return img


# A function that, after loading the image and model of the learned neural network,
# recognizes the animal and returns the result
def predict(filename):
    img = load_image(filename)
    model = load_model('dogs_and_cats_model.h5')
    result = model.predict(img)
    return result[0][0]
