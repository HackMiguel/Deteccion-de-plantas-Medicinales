import sys
import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K

K.clear_session()

data_entrenamiento = '/home/angel/Escritorio/ProyectoFinal/data/entrenamiento'
data_validacion = '/home/angel/Escritorio/ProyectoFinal/data/validacion'

epocas=20 #sin modificar
longitud, altura = 150, 150 #150,150 modificar
batch_size = 32#32
pasos = 250
validation_steps = 300 #250
filtrosConv1 = 32
filtrosConv2 = 64
tamano_filtro1 = (5, 5)#3*3 capa convolucional
tamano_filtro2 = (4, 4)#2*2
clases = 14 #15, 20
lr = 0.1 #modificado 05

##Preparamos nuestras imagenes, preprocesandolas
#Creamos un generador
entrenamiento_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.3,
    zoom_range=0.3,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

entrenamiento_generador = entrenamiento_datagen.flow_from_directory(
    data_entrenamiento,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical')

validacion_generador = test_datagen.flow_from_directory(
    data_validacion,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical')


cnn = Sequential()
cnn.add(Convolution2D(input_shape=(150,150,3),filters=64,kernel_size=(3,3),padding="same", activation="relu"))
cnn.add(Convolution2D(filters=64,kernel_size=(3,3),padding="same", activation="relu"))
cnn.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
cnn.add(Convolution2D(filters=128, kernel_size=(3,3), padding="same", activation="relu"))
cnn.add(Convolution2D(filters=128, kernel_size=(3,3), padding="same", activation="relu"))
cnn.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
cnn.add(Convolution2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
cnn.add(Convolution2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
cnn.add(Convolution2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
cnn.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
cnn.add(Convolution2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
cnn.add(Convolution2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
cnn.add(Convolution2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
cnn.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))

cnn.add(Flatten())
cnn.add(Dense(units=4096,activation="relu"))
cnn.add(Dense(units=4096,activation="relu"))
cnn.add(Dense(units=clases, activation="softmax"))
# queremos 14 salidas que son los posibles resultados de la clasificacion
cnn.compile(loss='categorical_crossentropy',
            optimizer=optimizers.Adam(lr=lr),
            metrics=['accuracy'])



#Entrenar algoritmo
cnn.fit_generator(
    entrenamiento_generador,
    steps_per_epoch=pasos,
    epochs=epocas,
    validation_data=validacion_generador,
    validation_steps=validation_steps)

target_dir = '/home/angel/Escritorio/ProyectoFinal/modelo/'
if not os.path.exists(target_dir):
  os.mkdir(target_dir)
cnn.save('/home/angel/Escritorio/ProyectoFinal/modelo/modelo.h5')
cnn.save_weights('/home/angel/Escritorio/ProyectoFinal/modelo/pesos.h5')
#os.system('poweroff')
