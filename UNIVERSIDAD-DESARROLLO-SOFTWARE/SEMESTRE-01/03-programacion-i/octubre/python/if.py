#condicionales simples
edad = int(input("Ingresa tu edad: "))

if edad == 30:
    print("Tienes 30 años")
else:
    print("No tienes 30 años")

#calificaion de un examen: de 9 a 10 sobresaliente, de 7 a 8 bueno, de 5 a 6 suficiente, menos de 5 insuficiente
nota = float(input("Ingresa tu calificación: "))

esSobreliente = nota >= 9 and nota <= 10
esBueno = nota >= 7 and nota < 9
esSuficiente = nota >= 5 and nota < 7
esInsuficiente = nota < 5 and nota >= 0

if esSobreliente:
    print("Sobresaliente")
elif esBueno:
    print("Bueno")
elif esSuficiente:
    print("Suficiente")
elif esInsuficiente:
    print("Insuficiente")
else:
    print("Calificación no válida")