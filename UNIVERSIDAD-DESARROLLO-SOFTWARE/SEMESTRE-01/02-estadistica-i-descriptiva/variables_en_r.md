```
# VARIABLES
# c es un keyword para funciones
# es case sensitive
a = 1
a <- 2
3 -> a
b = a

# strings
hola = ("hola")

# boolean
bool = TRUE
class(bool)
1>0 & 1<10
1< 0 | 1<10

#vector
vector1 = c(1,2,3)
vector2 = c(1, "a", 2)

#dataframe 
tabla1 <- data.frame(row = c(1,2), col = c(3,4))

### listas
lista1 = list(vector2, tabla1)
for (v in lista1) {
  print(v)
}
#indexacion
vector1[3]
print(tabla1[2,2])
lista1[[1]]
```