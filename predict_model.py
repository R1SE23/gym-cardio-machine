# -*- coding: utf-8 -*-
"""cardiotest

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jw-2XhaAmHC2emX6qmxmWEU5VtyKbl9g?usp=sharing
"""

# !pip install --upgrade pip
# !pip install --upgrade tensorflow
# !pip install tensorflow_hub
# !pip install keras
# !pip install Pillow

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import urllib

import keras
from keras.preprocessing import image


# Create pipeline
def predictImage(pic_name):
    # Labels
    dataset_labels = [
       'Elliptical', 
       'Stationary Bicycle',
       'Treadmill']

    #Load model
    modFile = 'cardio-classifier.h5'
    mod = tf.keras.models.load_model(modFile,custom_objects={'KerasLayer':hub.KerasLayer})
    # input image
    img = image.load_img(pic_name, target_size=(224, 224))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.    

    y_prob = mod.predict(img_tensor)
    y_classes = y_prob.argmax(axis=-1)
    res = dataset_labels[y_classes[0]]
    return res, y_prob


def loadImage(URL):
    img_path = 'temp.jpg'
    with urllib.request.urlopen(URL) as url:
        with open(img_path, 'wb') as f:
            f.write(url.read())
    return img_path
  
def predictImageFromURL(img_url):
    img_path = loadImage(img_url)
    res, y_prob = predictImage(img_path)
    return res, y_prob

##--------------------------------##
##----------- Test ---------------##
##--------------------------------##
#print('The result is: {}.'.format(predictImage('uploads/image1.jpg')))

img_url = 'https://images.prod.meredith.com/product/3eb95f095dbdea1caf123d1729279f19/1541651615506/l/hascon-exercise-bike-indoor-cycle-exercise-indoor-bike-for-workout-fitness'
print('The result is: {}.'.format(predictImageFromURL(img_url)))
