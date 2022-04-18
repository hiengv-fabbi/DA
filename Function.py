from __future__ import division
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras import layers
model = tf.keras.applications.VGG16(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
)
# model.summary()

def feat(img_path):
  # img_path = '/content/drive/MyDrive/Colab Notebooks/picture/HoaQua/10.jpg'
  img = image.load_img(img_path, target_size=(224, 224))
  img_data = image.img_to_array(img)
  img_data = np.expand_dims(img_data, axis=0)
  img_data = preprocess_input(img_data)

  vgg16_feature = model.predict(img_data)
  vgg16_feature_np = np.array(vgg16_feature)[0]
  vgg16_feature_array = vgg16_feature_np.flatten()
  # print(vgg16_feature_array)
  return np.array(vgg16_feature_array)

def Average(lst):
    return sum(lst) / len(lst)