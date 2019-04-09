from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.utils import to_categorical

#download mnist data and split into train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#plot the first image in the dataset
plt.imshow(X_train[0])

X_train[0].shape

X_train = X_train.reshape(60000,28,28,1)
X_test = X_test.reshape(10000,28,28,1)

#one-hot encode target column
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

model = Sequential()
#add model layers
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28,28,1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

#compile model using accuracy to measure model performance
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#train the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=2)

results = model.evaluate(X_test, y_test)

print('Final test set loss: {:4f}'.format(results[0]))
print('Final test set accuracy: {:4f}'.format(results[1]))

ypred = model.predict(X_test)

amount_of_pred_images=10000

#predict  images in the test set
num_acertos=0
for i in range(len(ypred)):
  for j in range(0, 9, 1):
    if ((ypred[i][j] == 1) and (y_test[i][j] == 1)):     
      num_acertos=num_acertos+1    

tot=num_acertos/amount_of_pred_images
print("num_acertos: ",num_acertos, "total: 10000", "perc: ", tot )    
