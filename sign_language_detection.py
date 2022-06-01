

import csv
import string
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator, array_to_img


TRAINING_FILE = 'C:\\Users\\rmzn\\Desktop\\sign_mnist_train.csv'
VALIDATION_FILE = 'C:\\Users\\rmzn\\Desktop\\sign_mnist_test.csv'

with open(TRAINING_FILE) as training_file:
  line = training_file.readline()
  print(f"First line (header) looks like this:\n{line}")
  line = training_file.readline()
  print(f"Each subsequent line (data points) look like this:\n{line}")


def parse_data_from_input(filename):
    with open(filename) as file:
        csv_reader = csv.reader(file, delimiter=',')

        next(csv_reader)
        labels = []
        images = []
        k = 1
        for line in csv_reader:
            labels.append(line[0])
            images.append(np.reshape(line[1:], (28, 28)))
        np_labels = np.asarray(labels)
        labels = np_labels.astype(float)
        np_images = np.asarray(images)
        images = np_images.astype(float)

        return images, labels

training_images, training_labels = parse_data_from_input(TRAINING_FILE)
validation_images, validation_labels = parse_data_from_input(VALIDATION_FILE)

print(f"Training images has shape: {training_images.shape}")
print(f"Training labels has shape: {training_labels.shape}")
print(f"Validation images has shape: {validation_images.shape}")
print(f"Validation labels has shape: {validation_labels.shape}")


def train_val_generators(training_images, training_labels, validation_images, validation_labels):

    training_images = np.expand_dims(training_images, axis=3)
    validation_images = np.expand_dims(validation_images, axis=3)

    train_datagen = ImageDataGenerator(rescale=1 / 255,
                                       rotation_range=40,
                                       width_shift_range=0.2,
                                       height_shift_range=0.2,
                                       shear_range=0.2,
                                       zoom_range=0.2,
                                       horizontal_flip=True,
                                       fill_mode='nearest')

    train_generator = train_datagen.flow(x=training_images,
                                         y=tf.keras.utils.to_categorical(training_labels, 26),
                                         batch_size=32)

    validation_datagen = ImageDataGenerator(rescale=1 / 255)

    validation_generator = validation_datagen.flow(x=validation_images,
                                                   y=tf.keras.utils.to_categorical(validation_labels, 26),
                                                   batch_size=32)


    return train_generator, validation_generator


train_generator, validation_generator = train_val_generators(training_images, training_labels, validation_images, validation_labels)

print(f"Images of training generator have shape: {train_generator.x.shape}")
print(f"Labels of training generator have shape: {train_generator.y.shape}")
print(f"Images of validation generator have shape: {validation_generator.x.shape}")
print(f"Labels of validation generator have shape: {validation_generator.y.shape}")


def create_model():

    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(26, activation='softmax')

    ])

    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])


    return model

model = create_model()

history = model.fit(train_generator,
                    epochs=15,
                    validation_data=validation_generator)