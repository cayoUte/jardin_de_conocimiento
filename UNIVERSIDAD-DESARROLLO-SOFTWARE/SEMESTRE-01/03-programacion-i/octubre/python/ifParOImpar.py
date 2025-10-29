#es par o impar
n = int(input("Ingresa un número entero: "))
esPar = n % 2 == 0
if esPar:
    print(f"El número {n} es par")
else:
    print(f"El número {n} es impar")
