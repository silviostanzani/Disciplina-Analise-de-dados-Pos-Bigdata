Aula 3

## Diagonóstico de modelo
```
adv <- read.csv("/home/silvio/courseAtSenac/DB/Advertising.csv", header = TRUE, colClasses = c("NULL", NA, NA, NA, NA)); 
head(adv);
summary(adv);
attach(adv);

adv.lm4 <- lm(sales ~ newspaper+radio+TV);
summary(adv.lm4);

adv.lm5 <- lm(sales ~ radio*TV);
summary(adv.lm5);
```

## Relação não lineares
```
autos <- read.csv("/home/senac/test/DB/auto.csv")
names(autos)
attach(autos)
summary(autos)
par(mfrow=c(1, 1))

cars.lm1 <- lm(mpg ~ horsepower , data = autos);
summary(cars.lm1);

plot(autos$horsepower, autos$mpg )
abline(cars.lm1,col="blue");

cars.lm2 <- lm(mpg ~ poly(horsepower,2), data = autos);
points(autos$horsepower, cars.lm2$fitted.values, col="orange" );

cars.lm3 <- lm(mpg ~ poly(horsepower,5), data = autos);
points(autos$horsepower, cars.lm3$fitted.values, col="red" );
```

```
install.packages("ggplot2")
```

## Outliers

```
houses=read.csv("/home/senac/test/DB/housing-train.csv",header=T,na.strings="?")
names(houses)
head(houses);
summary(houses);

findOutlier <- function(data, cutoff = 3) {
  ## Calculate the sd
  sds <- apply(data, 2, sd, na.rm = TRUE)
  ## Identify the cells with value greater than cutoff * sd (column wise)
  result <- mapply(function(d, s) {
    which(d > cutoff * s)
  }, data, sds)
  result
}

outliers <- findOutlier(houses)
outliers

removeOutlier <- function(data, outliers) {
  result <- mapply(function(d, o) {
    res <- d
    res[o] <- NA
    return(res)
  }, data, outliers)
  return(as.data.frame(result))
}

dataFilt <- removeOutlier(houses, outliers)
par (mfrow=c(2,1))
plot(predict(houses.lm1), residuals(houses.lm1))
plot(predict(dataFilt.lm1), residuals(dataFilt.lm1))
```
