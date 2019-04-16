from keras.callbacks import ModelCheckpoint
from keras.models import Model, load_model, save_model, Sequential
from keras.layers import Dense, Activation, Dropout, Input, Masking, TimeDistributed, LSTM, Conv1D
from keras.layers import GRU, Bidirectional, BatchNormalization, Reshape
from keras.optimizers import Adam
from keras.backend.tensorflow_backend import set_session
import tensorflow as tf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn

import sklearn
import numpy as np
from sklearn.preprocessing import StandardScaler
config = tf.ConfigProto()
config.gpu_options.allow_growth = True  

# dynamically grow the memory used on the GPUconfig.log_device_placement = True  # to log device placement (on which device the operation ran)
sess = tf.Session(config=config)
tf.keras.backend.set_session(sess)  # set this TensorFlow session as the default session for Keras


# Read in white wine data 
white = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=';')
# Read in red wine data 
red = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=';')

# Print info on white wine
print(white.info())
# Print info on red wine
print(red.info())
# First rows of `red` 
red.head()
# Last rows of `white`
white.tail()
# Take a sample of 5 rows of `red`
red.sample(5)
# Describe `white`
white.describe()
# Double check for null values in `red`
pd.isnull(red)

# Add `type` column to `red` with value 1
red['type'] = 1
# Add `type` column to `white` with value 0
white['type'] = 0
# Append `white` to `red`
wines = red.append(white, ignore_index=True)

# Import `train_test_split` from `sklearn.model_selection`
from sklearn.model_selection import train_test_split
# Specify the data 
X=wines.ix[:,0:11]
# Specify the target labels and flatten the array
y= np.ravel(wines.type)
# Split the data up in train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# Define the scaler 
scaler = StandardScaler().fit(X_train)
# Scale the train set
X_train = scaler.transform(X_train)
# Scale the test set
X_test = scaler.transform(X_test)


from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(12, activation='relu', input_shape=(11,)))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.output_shapemodel.summary()
model.get_config()
model.get_weights()

model.compile(loss='binary_crossentropy',              optimizer='adam',              metrics=['accuracy'])
model.fit(X_train, y_train,epochs=20, verbose=1)

y_pred = model.predict(X_test)

print(y_pred[:5])
print(y_test[:5])

score = model.evaluate(X_test, y_test,verbose=1)
print(score)






