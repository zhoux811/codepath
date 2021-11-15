import os

#os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
import cv2
import random

import keras.losses
import tqdm

import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Activation, Flatten
from tensorflow.keras.models import Sequential


def img2arr(path):
    img_array = cv2.imread(path)  # convert to array
    img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
    return img_array


IMG_SIZE = 200


def ImgArrResized(path, new_size):
    new_array = cv2.resize(img2arr(path), (new_size, new_size))
    return new_array


ImgArrResized('C:User/shio/Downloads/insects/train/dragonflies/1113001.jpg', IMG_SIZE)

training_data = []


def create_training_data():
    for category in ['dragonflies', 'cockroach', 'beetles']:
        # create path to ['dragonflies','cockroach', 'beetles', ]
        path = os.path.join('Downloads/insects/train/', category)
        # get the classification# 0=dragonflies, 1=cockroach, 2=beetles
        class_num = ['dragonflies', 'cockroach', 'beetles'].index(category)
        for img in tqdm.tqdm(os.listdir(path)):
            try:
                training_data.append(
                    [ImgArrResized(os.path.join(path, img), IMG_SIZE), class_num])  # add this to our training_data
            except Exception as e:  # in the interest in keeping the output clean...
                print('append failed at : ' + os.path.join(path, img))
                break


create_training_data()

random.shuffle(training_data)

x_train = []
y_train = []

for features, label in training_data:
    x_train.append(features)
    y_train.append(label)

x_train = np.array(x_train).reshape(-1, IMG_SIZE, IMG_SIZE, 3)
y_train = np.asarray(y_train)

x_train = x_train / 255.0

model = Sequential()

model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))


model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(1))

# keras.losses.categorical_hinge()
# keras.optmizers.
model.compile(loss='categorical_hinge', optimizer='adam', metrics=['accuracy'])

model.fit(x=x_train, y=y_train, batch_size=16, epochs=25, validation_split=0.1)
