## Aula 2

### Demonstrações

## Visualizar dados históricos de vendas de imóveis
```
library(corrplot)
library(e1071)

houses=read.csv("/home/senac/test/DB/housing-train.csv",header=T,na.strings="?")
names(houses)
head(houses);
summary(houses);
par (mfrow=c(1,1))
```

## Exemplos de relações lineares e não-lineares para identificar o preço
```
scatter.smooth(x=houses$s, y=houses$p, main="size ~ price")  # scatterplot
scatter.smooth(x=houses$be, y=houses$p, main="Bedrooms ~ price")  # scatterplot
```

## Aplicando Regressão Linear

```
houses.lm1 <- lm(p ~ s, data = houses);
coefficients(houses.lm1) # Model coefficients
```

## Avaliando a qualidade do Modelo
```
par ( mfrow = c (1 ,1) )
plot(houses$s,houses$p)
abline(houses.lm1);

summary(houses.lm1);
```
