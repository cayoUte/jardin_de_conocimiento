#validar si n es positivo, negativo o cero
n = float(input("Ingresa un número: "))
esPositivo = n > 0
esNegativo = n < 0
esCero = n == 0
if esPositivo:
    print("El número es positivo")
elif esNegativo:
    print("El número es negativo")
elif esCero:
    print("El número es cero")
else:
    print("Valor no válido")

#validar si un año es bisiesto
año = int(input("Ingresa un año: "))
esBisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
if esBisiesto:
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")
    
#validar si un carácter es vocal o consonante
caracter = input("Ingresa un carácter: ").lower()
esVocal = caracter in ['a', 'e', 'i', 'o', 'u']
esConsonante = caracter.isalpha() and not esVocal
if esVocal:
    print(f"El carácter '{caracter}' es una vocal")
elif esConsonante:
    print(f"El carácter '{caracter}' es una consonante")        