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

## transformandor para factor

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


