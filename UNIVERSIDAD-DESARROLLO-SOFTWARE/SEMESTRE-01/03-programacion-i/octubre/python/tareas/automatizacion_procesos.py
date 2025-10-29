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
	print(divider)
	print("Cálculo de sueldos")
	print(divider_1)
	hours = float(input("Ingrese el numero de horas trabajadas: "))
	daily_wage = 0
	select_rate = input("Seleccione la tarifa por hora (A: $10.00, B: $15.00, C: $20.00): ").upper()
	if select_rate == 'A':
		daily_wage = hours * 10.00  # Sueldo diario a $10 por hora
    elif select_rate == 'B':
		daily_wage = hours * 15.00  # Sueldo diario a $15 por hora
	elif select_rate == 'C':
		daily_wage = hours * 20.00  # Sueldo
	daily_wage = hours * 15.00  # Sueldo diario a $15 por hora
	monthly_wage = daily_wage * 30
	annual_wage = daily_wage * 365
	print(f"Sueldo mensual: ${monthly_wage:.2f}")
	print(f"Sueldo anual: ${annual_wage:.2f}")
