

from keras.applications.vgg16 import VGG16
model = VGG16()

# here in input 3 rgb and in conv1 64 (3*3) filter
model.summary()

from keras.saving.legacy.saved_model import load
from keras.preprocessing.image import load_img
from tensorflow.keras.utils import load_img
from keras.applications.imagenet_utils import preprocess_input
import numpy as np

image = load_img('rose.jpg',target_size=(224,224))
image = np.array(image)

from keras.saving.legacy.saved_model import load
from keras.preprocessing.image import load_img
from tensorflow.keras.utils import load_img
from keras.applications.imagenet_utils import preprocess_input
import numpy as np

image = load_img('rose.jpg',target_size=(224,224))
image = np.array(image)

from keras.saving.legacy.saved_model import load
#from keras.preprocessing.image import load_img
from tensorflow.keras.utils import load_img
from keras.applications.imagenet_utils import preprocess_input
import numpy as np

image = load_img('rose.jpg',target_size=(224,224))
image = np.array(image)

image = image.reshape((1,image.shape[0],image.shape[1],image.shape[2]))

image = preprocess_input(image)
image
#my_image=imread('rose.jpg')
#imshow(my_image)

yhat=model.predict(image)

from keras.applications.vgg16 import preprocess_input,decode_predictions
label=decode_predictions(yhat)
label
