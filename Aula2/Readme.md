## Aula 2

### Demonstrações

## Visualizar dados históricos de vendas de imóveis
```
houses <- read.csv(url("https://raw.githubusercontent.com/silviostanzani/PosBigData/master/housing-train.csv"))

names(houses)
head(houses);
summary(houses);
```

## Exemplos de relações lineares e não-lineares para identificar o preço
```
par (mfrow=c(2,1))
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


## Carregando Dados da Base Advertising
```
adv <- read.csv("/home/silvio/courseAtSenac/DB/Advertising.csv", header = TRUE, colClasses = c("NULL", NA, NA, NA, NA)); 
head(adv);
summary(adv);
attach(adv);
```

## Aplicando Regressão Linear comparando Vendas e investimento em TV
```
par (mfrow=c(3,1))
adv.lm1 <- lm(sales ~ TV);
summary(adv.lm1);
plot(TV,sales)
abline(adv.lm1);

```

## Aplicando Regressão Linear comparando Vendas e investimento em Radio
```

adv.lm2 <- lm(sales ~ radio);
summary(adv.lm2);
plot(radio,sales)
abline(adv.lm2);

```

## Aplicando Regressão Linear comparando Vendas e investimento em Jornal
```

adv.lm3 <- lm(sales ~ newspaper);
summary(adv.lm3);
plot(newspaper,sales)
abline(adv.lm3);
```

## Avaliando correlação entre variáveis preditoras
```
cor(adv)
```

## Regressão com Mũltiplas Variáveis
```
adv.lm4 <- lm(sales ~ newspaper+radio+TV);
summary(adv.lm4);
```
