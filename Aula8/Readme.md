# Aula 8

## Rede Neural para reconhecimento de imagem usando MLP
```
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical
```

# Preparação de dados para rede MLP
* Normalização entre 0 e 1 - todos os valores são divididos por 255.
```
num_classes = 10
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')/255
x_test = x_test.astype('float32') /255

# convert class vectors to binary class matrices
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)
```
* Montando modelo 

```
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
#model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
#model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))

print(model.summary())

batch_size = 64
epochs = 5
```

* Compilando e rodando o modelo

```
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))
```
* Avaliando o modelo
```
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])


```

## Rede Neural para reconhecimento de imagem usando convnet - CNN (Convolution neural network)
```
import tensorflow as tf

from keras import layers
from keras import models
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout


# Preparação para CNN
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape((60000, 28, 28, 1))
x_train = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28, 28, 1))
x_test = test_images.astype('float32') / 255

y_train = to_categorical(train_labels)
y_test = to_categorical(test_labels)


# Rede CNN
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

print(model.summary())

batch_size = 64
epochs = 5

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))


score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

```

## Inferência utilizando Redes Neurais Convolucionais Treinadas
```
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16


from keras.applications import ResNet50
from keras.applications import InceptionV3
from keras.applications import Xception # TensorFlow ONLY
from keras.applications import VGG16
from keras.applications import VGG19
from keras.applications import imagenet_utils
```

* Carrega Modelo
```
#model = VGG16()
#model = VGG19()
model = InceptionV3()
#model = Xception()
#model = ResNet50
```

* Carrega imagem do arquivo
```
#image = load_img('/home/silvio/mug.jpg', target_size=(224, 224))
image = load_img('/home/silvio/mug.jpg', target_size=(299, 299))
```

```
# Converter pixels em um array
image = img_to_array(image)

# acertar formato do array para o modelo
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

# preprocessamento da imagem
image = preprocess_input(image)

# calcular probabilidade considerando todos os "labels"
yhat = model.predict(image)

# Codificar as probabilidades retornadas nos "labels"
label = decode_predictions(yhat)


for (i, (imagenetID, label, prob)) in enumerate(label[0]):
	print("{}. {}: {:.2f}%".format(i + 1, label, prob * 100))




# obtém identificação da imagem (Label)
#label = label[0][0]

# Classificação
#print('%s (%.2f%%)' % (label[1], label[2]*100))
```

* Inferencia com rede inception
```
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.applications.inception_v3 import *
import numpy as np

model = InceptionV3(weights='imagenet')

img = image.load_img('/home/silvio/mug.jpg', target_size=(299, 299))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

y = model.predict(x)
for index, res in enumerate(decode_predictions(y)[0]):
    print('{}. {}: {:.3f}%'.format(index + 1, res[1], 100 * res[2]))

```
Exercícios
1) Altere a rede neural MLP para classificar dígitos (Mnist) para utilizar 3 camadas densas (com 10 neuronios cada uma). A acurácia fica diferente em relação a rede do código original?

2) Altere a rede neural CNN para classificar dígitos (Mnist) nas duas primeiras camadas conv2d e pooling, use convolução 4x4 e pooling 3x3. A acurácia fica diferente em relação a rede do código original?

3) teste a inferência usando diferentes imagens e redes pré-treinandas.

4) obtenha a foto de uma pessoa no site https://www.thispersondoesnotexist.com/ e verifique se a rede neural reconhece como sendo uma pessoa
