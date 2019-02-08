# SenacBigData

## Aula 1

### Demonstrações

Relação não-linear
``
Temperature <- c(50, 48, 47, 21, 20.7, 20.5,19.8,19.3, 19.1, 18.9 )
Time <- c(1, 2, 3, 4, 5,6,7,8,9,10)

plot(Time,Temperature, verticals=TRUE)
``

Relação linear
``
head(cars) 
names(cars) 
show(cars) 
scatter.smooth(x=cars$speed, y=cars$dist, main="Stop Distance ~ Speed")  # scatterplot
``

### Atividades

#### Instalar rstudio
curl -O https://download1.rstudio.org/rstudio-xenial-1.1.463-amd64.deb
sudo gdebi rstudio-xenial-1.1.463-amd64.deb

