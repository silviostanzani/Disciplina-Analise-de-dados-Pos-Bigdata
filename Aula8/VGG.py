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

# Carrega Modelo
#model = VGG16()
#model = VGG19()
model = InceptionV3()
#model = Xception()
#model = ResNet50

# Carrega imagem do arquivo
image = load_img('/home/silvio/mug.jpg', target_size=(224, 224))
#image = load_img('/home/silvio/mug.jpg', target_size=(299, 299))



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

