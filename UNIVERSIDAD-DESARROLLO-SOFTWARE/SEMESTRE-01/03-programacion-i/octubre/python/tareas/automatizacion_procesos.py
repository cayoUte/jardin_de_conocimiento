# ...existing code...
# La empresa XYZ necesita automatizar los siguientes procesos:
# -Control de temperatura
# -Valor de sueldos(diario, mensual, anual)
# -Calculo de areas y perimetro de 4 figuras basicas

    
company_name = "Construcciones XYZ"

divider = "=" * 50
divider_1 = "-" * 50
print(divider)
print(f"Bienvenido a {company_name}")
print(divider)
print("\nSeleccione el proceso que desea realizar:")
print(divider_1)
print("1. Control de temperatura")
print("2. Cálculo de sueldos")
print("3. Cálculo de áreas y perímetros de figuras básicas")
print("4. Salir")
option = int(input("Ingrese el número de la opción deseada (1-4): "))
current_temperature = None
if option == 1:
    # Control de temperatura
    print(divider)
    print("Control de temperatura")
    print(divider_1)
    current_temperature = float(input("Ingrese la temperatura en grados Celsius: "))
    print(f"Ajustando la temperatura a {current_temperature}°C...")
    if current_temperature < 0:		
        print("La temperatura es muy baja. Riesgo de congelación.")
    elif 0 <= current_temperature <= 15:
        print("La temperatura es baja. Se recomienda abrigarse.")
    elif 16 <= current_temperature <= 25:
        print("La temperatura es agradable.")
    elif 26 <= current_temperature <= 35:
        print("La temperatura es alta. Manténgase hidratado.")
    else:
        print("La temperatura es muy alta. Riesgo de golpe de calor.")
elif option == 2:
    # Cálculo de sueldos
    print(divider)
    print("Cálculo de sueldos")
    print(divider_1)
    hours = float(input("Ingrese el numero de horas trabajadas: "))
    daily_wage = 0
    print("Tarifa por hora A: $10.00, B: $15.00, C: $20.00")
    selected_rate = input("Seleccione A, B o C: ").upper()
    if selected_rate == 'A':
        daily_wage = hours * 10.00  # Sueldo diario a $10 por hora
    elif selected_rate == 'B':
        daily_wage = hours * 15.00  # Sueldo diario a $15 por hora
    elif selected_rate == 'C':
        daily_wage = hours * 20.00  # Sueldo diario a $20 por hora
    monthly_wage = daily_wage * 30
    annual_wage = daily_wage * 365
    print(f"Sueldo diario: ${daily_wage:.2f}")
    print(f"Sueldo mensual: ${monthly_wage:.2f}")
    print(f"Sueldo anual: ${annual_wage:.2f}")
elif option == 3:
    # Cálculo de áreas y perímetros de figuras básicas
	print(divider)
	print("Cálculo de áreas y perímetros de figuras básicas")
	print(divider_1)
	print("Seleccione la figura:")
	print("1. Cuadrado")
	print("2. Rectángulo")
	print("3. Círculo")
	print("4. Triángulo")
	shape_option = int(input("Ingrese el número de la figura deseada (1-4): "))
	if shape_option == 1:
		side = float(input("Ingrese la longitud del lado del cuadrado: "))
		area = side ** 2
		perimeter = 4 * side
		print(f"Área del cuadrado: {area}")
		print(f"Perímetro del cuadrado: {perimeter}")
	elif shape_option == 2:
		length = float(input("Ingrese la longitud del rectángulo: "))
		width = float(input("Ingrese el ancho del rectángulo: "))
		area = length * width
		perimeter = 2 * (length + width)
		print(f"Área del rectángulo: {area}")
		print(f"Perímetro del rectángulo: {perimeter}")
	elif shape_option == 3:
		radius = float(input("Ingrese el radio del círculo: "))
		area = 3.1416 * radius ** 2
		perimeter = 2 * 3.1416 * radius
		print(f"Área del círculo: {area}")
		print(f"Perímetro del círculo: {perimeter}")
	elif shape_option == 4:
		print("Tipos de triángulos: 1. Equilátero 2. Isósceles 3. Escaleno")
		triangle_type = int(input("Seleccione el tipo de triángulo (1-3): "))
		if triangle_type == 1:
			side = float(input("Ingrese la longitud del lado del triángulo equilátero: "))
			area = (3 ** 0.5 / 4) * side ** 2
			perimeter = 3 * side
			print(f"Área del triángulo equilátero: {area}")
			print(f"Perímetro del triángulo equilátero: {perimeter}")
			exit()
		elif triangle_type == 2:
			base = float(input("Ingrese la base del triángulo isósceles: "))
			side = float(input("Ingrese la longitud de los lados iguales del triángulo isósceles: "))
			triangle_inequality = 2 * side > base
			if not triangle_inequality:
				print("Los valores ingresados no forman un triángulo isósceles válido.")
				exit()

			height = (side ** 2 - (base / 2) ** 2) ** 0.5
			area = 0.5 * base * height
			perimeter = 2 * side + base
			print(f"Área del triángulo isósceles: {area}")
			print(f"Perímetro del triángulo isósceles: {perimeter}")
			exit()
		elif triangle_type == 3:
			base = float(input("Ingrese la base del triángulo escaleno: "))
			side_a = float(input("Ingrese el lado a del triángulo escaleno: "))
			side_b = float(input("Ingrese el lado b del triángulo escaleno: "))
			triangle_inequality = (side_a + side_b > base) and (side_a + base > side_b) and (side_b + base > side_a)
			if not triangle_inequality:
				print("Los valores ingresados no forman un triángulo escaleno válido.")
				exit()
			#Semiperimetro
			s = (base + side_a + side_b) / 2
			#Área usando la fórmula de Herón
			area = (s * (s - base) * (s - side_a) * (s - side_b)) ** 0.5
			perimeter = base + side_a + side_b
			print(f"Área del triángulo escaleno: {area}")
			print(f"Perímetro del triángulo escaleno: {perimeter}")
			exit()		 
	else:
		print("Opción de figura no válida.")
elif option == 4:
	print("Saliendo del programa. ¡Hasta luego!")
else:
	print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")