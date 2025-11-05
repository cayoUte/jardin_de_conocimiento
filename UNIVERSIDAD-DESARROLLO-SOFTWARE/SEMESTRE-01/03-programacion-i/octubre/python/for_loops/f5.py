#Quiero saber cuantas veces se usa la vocal a
# en una frase

frase = "El dia de hoy esta mucho frio en quito, chachai"

#Contador
#Condicional
#Iterar

contador = 0

for vocal in frase:
    if vocal == "a":
        contador += 1

print("El total de letras es: ", contador)