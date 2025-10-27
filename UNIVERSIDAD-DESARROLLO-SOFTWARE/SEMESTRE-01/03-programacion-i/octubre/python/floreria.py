# Floreria Juanita
# -Desea vender 3 tipos de flores
# -Que informe si el valor supera los $50
# -Si supera le hace un descuento del 10%

separador = "-" * 40
separador2 = "=" * 40
nombre_tienda = "FLORERIA JUANITA"
informar_descuento = lambda: print("Nuestra oferta del dia de hoy es: por la compra superior a los $50 te llevas un descuento del 10%")
dar_bienvenida = lambda nombre_tienda: print("Bienvenido a ", nombre_tienda)
preguntar_nombre = lambda: input("Ingrese su nombre: ")
preguntar_compra = lambda: input("Desea comprar flores? (si/no): ").lower()
preguntar_tipo_flor = lambda: input("Ingrese el tipo de flor que desea 1, 2, 3: ")
florOrquidea = "Orquideas"
florTulipan = "Tulipanes"
florGirasol = "Girasoles"
finalizar_compra = 4
precioOrquidea = 20.0
precioTulipan = 15.0
precioGirasol = 10.0

#bienvenida
print(separador2)
dar_bienvenida(nombre_tienda)
print(separador2)

#preguntar nombre
nombre_cliente = preguntar_nombre()
print(separador)

#preguntar si desea comprar flores
desea_comprar = preguntar_compra()

if desea_comprar == "si":
    print(separador)
    print("Excelente ", nombre_cliente, ", tenemos las siguientes flores disponibles:")
    print(separador)
    print("Menu de flores:")
    print(separador)
    print("1. ", florOrquidea, " - $", precioOrquidea)
    print("2. ", florTulipan, " - $", precioTulipan)
    print("3. ", florGirasol, " - $", precioGirasol)
    print("finalizar compra: ", finalizar_compra)
    print(separador)
    carrito_compras = []
    tipo_flor = 0
    flor_elegida = 0
    total = 0.0
    def calcular_total(carrito):
        suma = 0.0
        for precio in carrito:
            suma += precio
        return suma
    while flor_elegida != 4:
        
        tipo_flor = preguntar_tipo_flor()

        match tipo_flor:        
            case "1":
                precio_flor = precioOrquidea
                flor_elegida = 1
                
            case "2":
                precio_flor = precioTulipan
                flor_elegida = 2
                
            case "3":
                precio_flor = precioGirasol
                flor_elegida = 3
                
            case "4":
                print("Has decidido finalizar la compra sin seleccionar flores.")
                precio_flor = 0 
                flor_elegida = 4
            case _:
                print("Tipo de flor no valido.")
                precio_flor = 0 
                flor_elegida = 0
                
        if flor_elegida != 4 and precio_flor > 0:
            print(separador)
            print("Has elegido la flor tipo ", flor_elegida, " con un precio de $", precio_flor)
            carrito_compras.append(precio_flor)
            print("Flor agregada al carrito.")
            print("Total parcial: $", calcular_total(carrito_compras))
        if flor_elegida == 0:
            print("Por favor, elija una opcion valida.")
    if len(carrito_compras) > 0:
        total = calcular_total(carrito_compras)
        print(separador2)
        print("El total de su compra es: $", total)
        if total > 50:
            descuento = total * 0.10
            total_con_descuento = total - descuento
            print("Felicidades! Su compra supera los $50, por lo que recibe un descuento del 10%: -$", descuento)
            print("Total con descuento: $", total_con_descuento)
        else:
            print("Su compra no supera los $50, no aplica descuento.")
            
        print(separador)
        print("Gracias por su compra, ", nombre_cliente, ". Vuelva pronto!")
else:
    print("Gracias por visitarnos, ", nombre_cliente, ". Vuelva pronto!")
    