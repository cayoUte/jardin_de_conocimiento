#   Ejercicis
#   1. Imprime los números del 1 al 10 usando un bucle for.
for numero in range(1, 11):
    print(numero)
# Deletrea la palabra "Abecedario" letra por letra usando un bucle for.
palabra = "Abecedario"
for letra in palabra:
    print(letra)
# Imprime los primeros 5 numeros elevados al cuadrado usando un bucle for.
for num in range(1, 6):
    print(num ** 2)

#imprime el contenido de una lista
Lista = ["fjsdk", "2", "3", "4", "5", 5, False, 1.5]

# Quiero que se muestren los numeros pares del uno al 20
for numero in range(1, 21): 
    if numero % 2 == 0:
        print(numero)
suma = 0        
for n in range(1, 101):
    suma += n 
print("La suma de los primeros 100 numeros es:", suma)
    