Aula 3

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
