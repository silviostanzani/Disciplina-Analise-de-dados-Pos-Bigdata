## Aula7

### Rede Neural Para Iris (classificação)

#### Fonte:  https://gist.github.com/NiharG15/cd8272c9639941cf8f481a7c4478d525

* Criar ambiente para desenvolvimento de rede neural usando Keras
```
* criar um ambiente conda (conda create -n NN)
* acessar o ambiente conda (source activate NN)
  * * acessar o ambiente conda (No windows)  (conda activate NN)
* Instalar pacote keras (conda install keras)
* Instalar pacote scikit-learn (conda install scikit-learn)
* Instalar Pandas (conda install pandas)
```

* Importando bibliotecas

```
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
```

# Preparação de Dados
```
iris_data = load_iris() # load the iris dataset

print('Example data: ')
print(iris_data.data[:5])
print('Example labels: ')
print(iris_data.target[:5])

x = iris_data.data
y_= iris_data.target.reshape(-1, 1) # Convert data to a single column

# Normalização
encoder = OneHotEncoder(sparse=False)
y = encoder.fit_transform(y_)
print(y[:5])

# Dividir em Treino e Teste
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.20)
```

# Construindo o modelo
```
model = Sequential()

model.add(Dense(10, input_shape=(4,), activation='relu', name='fc11'))
model.add(Dense(10, activation='relu', name='fc22'))
model.add(Dense(3, activation='softmax', name='output'))

optimizer = Adam(lr=0.001)
model.compile(optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

print('Neural Network Model Summary: ')
print(model.summary())
```

# Treinando o modelo
```
model.fit(train_x, train_y, verbose=2, epochs=200)
```

# Avaliação do Modelo
```
results = model.evaluate(test_x, test_y)

print('Final test set loss: {:4f}'.format(results[0]))
print('Final test set accuracy: {:4f}'.format(results[1]))
```

# Predição
* O retorno da predição é uma probabilidade associada a cada classe, e em seguida é feito arredondamento para obter a classe com maior probabilidade
```
test = np.array([[5.1, 3.5, 1.4, 0.2]])
print(test)
ynew = model.predict(test)
print(ynew)
ynew2=np.around(ynew,decimals=1)
print(ynew2)
```

# Segundo Exemplo - regressão auto - Código Completo
```
from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.model_selection import train_test_split
import io
import requests

url = "https://raw.githubusercontent.com/silviostanzani/PosBigData/master/Auto2.csv"
s = requests.get(url).content
dataframe = read_csv(io.StringIO(s.decode('utf-8')))

dataset = dataframe.values

# split into input (X) and output (Y) variables
X = dataset[:,2:8]
y = dataset[:,1]
print(X)
print(y)

train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.20)

model = Sequential()
model.add(Dense(20, input_dim=6, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))
# Compile model
model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(train_x, train_y, verbose=2, epochs=200)

results = model.evaluate(test_x, test_y)

print(results)
```
