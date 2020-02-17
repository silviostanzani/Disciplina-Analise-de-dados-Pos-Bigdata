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
## para dataset auto (https://raw.githubusercontent.com/silviostanzani/PosBigData/master/Auto2.csv)

* mpg	Miles/(US) gallon
* cyl	Number of cylinders
* disp	Displacement (cu.in.)
* hp	Gross horsepower
* drat	Rear axle ratio
* wt	Weight (lb/1000)
* qsec	1/4 mile time
* vs	V/S
* am	Transmission (0 = automatic, 1 = manual)
* gear	Number of forward gears
* carb	Number of carburetors

### Realize uma analise regressao linear para identificar mpg com base nas caracteristicas
* Monte um modelo de regressao com a variavel mais correlata a mpg
* Monte um modelo de regressao com todas as variaveis
* Compare os resultados obtidos (use R2 e grafico de residuos)
* Teste algumas combinacoes de variaveis preditoras usando o R2 e RSE como parâmetro
