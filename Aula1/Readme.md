## Aula 1

### Demonstrações

#### Relação não-linear

```
Temperature <- c(50, 48, 47, 21, 20.7, 20.5,19.8,19.3, 19.1, 18.9 )
Time <- c(1, 2, 3, 4, 5,6,7,8,9,10)

plot(Time,Temperature, verticals=TRUE)
```

#### Relação linear

```
head(cars) 
names(cars) 
show(cars) 
scatter.smooth(x=cars$speed, y=cars$dist, main="Stop Distance ~ Speed")  # scatterplot
```

#### Exploração de dados

##### Private : Public/private indicator
##### Apps : Number of applications received
##### Accept : Number of applicants accepted
##### Enroll : Number of new students enrolled
##### Top10perc : New students from top 10 % of high school class
##### Top25perc : New students from top 25 % of high school class
##### F.Undergrad : Number of full-time undergraduates
##### P.Undergrad : Number of part-time undergraduates
##### Outstate : Out-of-state tuition
##### Room.Board : Room and board costs
##### Books : Estimated book costs
##### Personal : Estimated personal spending
##### PhD : Percent of faculty with Ph.D.’s
##### Terminal : Percent of faculty with terminal degree
##### S.F.Ratio : Student/faculty ratio
##### perc.alumni : Percent of alumni who donate
##### Expend : Instructional expenditure per student
##### Grad.Rate : Graduation rate

#### Carregar dados

```
collegeData <- read.csv("https://raw.githubusercontent.com/silviostanzani/PosBigData/master/College.csv")
```

### Exercícios:

#### Visualizar dados - Quais os preditores qualitativos e quantitativos ?
```
fix ( collegeData )
names(collegeData)
summary(collegeData)
```
  
#### O que se pode afirmar a respeito do padrão de preços dos livros ao longo do curso
```
hist(collegeData$Books)
```

#### Filtro de dados em um dataframe
```
private <- collegeData[(collegeData$Private =="Yes"), ]
```



#### Gere um gráfico para comparar as taxas de alunos de fora do estado (Outstate) entre universidades públicas e privadas (Private)


#### Crie uma nova variável nesse conjunto de dados chamada elite que possui dois valores sim e não. Para SIM a universidade precisa ter mais de 30% dos alunos matriculados provenientes das escolas entre as 10% melhores escolas de ensino médio, caso contrário o campo elite é igual a nao. Quantas universidaades so de elite?

#### Indique dois pares de colunas do dataset college que apresentam relação linear entre si


