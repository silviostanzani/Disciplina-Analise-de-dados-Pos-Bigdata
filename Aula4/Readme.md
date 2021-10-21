## Aula 4

## Curva Sigmóide

```
sigmoid = function(x) {
  1 / (1 + exp(-x))
}

#x <- seq(-5, 5, 0.01)
mn=25
x <- rnorm(2000) #, mean = mn, sd = mn/3)

plot(x, sigmoid(x), col='blue')

```

## Instalar pacotes 
```
install.packages("mlbench")
install.packages("caret")
install.packages("tidyverse")
install.packages("car")
install.packages("ISLR")
```

## Identificar Classe de Cancer, Maligno ou Benigno
```
library('mlbench')
data(BreastCancer, package="mlbench")
bc <- BreastCancer[complete.cases(BreastCancer), ] 
summary(bc)

lrml <- glm(Class ~ Cell.shape, family="binomial", data = bc)
summary(lrml)
```

## Transformando para factor

```
bc <- bc[,-1]

# convert factors to numeric
for(i in 1:9) {
  bc[, i] <- as.numeric(as.character(bc[, i]))
}

bc$Class <- ifelse(bc$Class == "malignant", 1, 0)
bc$Class <- factor(bc$Class, levels = c(0, 1))

lrml2 <- glm(Class ~ Cell.shape, family="binomial", data = bc)
summary(lrml2)
```

## Base de treino e base de teste
```
library("caret")
set.seed(100)
trainDataIndex <- createDataPartition(bc$Class, p=0.7, list = F)  # 70% training data
trainData <- bc[trainDataIndex, ]
testData <- bc[-trainDataIndex, ]
```

## Otimizar número de classes
```
set.seed(100)
down_train <- downSample(x = trainData[, colnames(trainData) %ni% "Class"],  y = trainData$Class)

table(down_train$Class)

set.seed(100)
up_train <- upSample(x = trainData[, colnames(trainData) %ni% "Class"], y = trainData$Class)
```

## Diagnóstico de Modelos
```
logitmod <- glm(Class ~ Cl.thickness + Cell.size + Cell.shape, family = "binomial", data=down_train)
summary(logitmod)

logitmod2 <- glm(Class ~ Cl.thickness + Cell.size + Cell.shape, family = "binomial", data=bc)
summary(logitmod2)

logitmod3 <- glm(Class ~ Cl.thickness + Cell.size + Cell.shape, family = "binomial", data=trainData)
summary(logitmod3)
```

## Predição
```
pred <- predict(logitmod, newdata = testData, type = "response")

y_pred_num <- ifelse(pred > 0.5, 1, 0)
y_pred <- factor(y_pred_num, levels=c(0, 1))
y_act <- testData$Class

table(trainData$Class)
mean(y_pred == y_act)
```

## treino e predição breat cancer
```
data(BreastCancer, package="mlbench")
bc <- BreastCancer[complete.cases(BreastCancer), ] 

bc <- bc[,-1]

# convert factors to numeric
for(i in 1:9) {
  bc[, i] <- as.numeric(as.character(bc[, i]))
}

bc$Class <- ifelse(bc$Class == "malignant", 1, 0)
bc$Class <- factor(bc$Class, levels = c(0, 1))

library("caret")
set.seed(100)
trainDataIndex <- createDataPartition(bc$Class, p=0.7, list = F)  # 70% training data
trainData <- bc[trainDataIndex, ]
testData <- bc[-trainDataIndex, ]
```

## treino
```
logitmod3 <- glm(Class ~ Cl.thickness + Cell.size + Cell.shape, family = "binomial", data=trainData)
summary(logitmod3)
```

## avaliacao
```
pred <- predict(logitmod3, newdata = testData, type = "response")

y_pred_num <- ifelse(pred > 0.5, 1, 0)
y_pred <- factor(y_pred_num, levels=c(0, 1))
y_act <- testData$Class

table(trainData$Class)
mean(y_pred == y_act)
```


## LDA
```
#Exemplo 1

require(MASS)
data(iris)
head(iris, 100)

summary(iris)

r <- lda(formula = Species ~ ., data = iris)
r 

lda.train <- predict(r)
iris$lda <- lda.train$class
table(iris$lda,iris$Species)
```




Monte um modelo de regressao logistica e LDA para predizer a coluna income usando a base a seguir:

Colunas:

* age
* workclass
* fnlwgt
* education
* educational-num
* marital-status
* occupation
* relationship
* race
* gender
* capital-gain
* capital-loss
* hours-per-week
* native-country
* income

https://raw.githubusercontent.com/silviostanzani/PosBigData/master/adult.csv

Opcional: divida a base entre treino e teste e compare os resultados obtidos

Utilize o LDA para classificar o dataset a seguir de acordo com a coluna Class
https://raw.githubusercontent.com/MateLabs/Public-Datasets/master/Datasets/wine.csv
