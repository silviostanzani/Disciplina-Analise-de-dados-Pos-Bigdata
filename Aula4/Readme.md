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

