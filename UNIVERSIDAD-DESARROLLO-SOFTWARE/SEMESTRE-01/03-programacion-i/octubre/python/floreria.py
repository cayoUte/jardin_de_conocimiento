# Floreria Juanita
# -Desea vender 3 tipos de flores
# -Que informe si el valor supera los $50
# -Si supera le hace un descuento del 10%
import os

def clear_terminal():
    """Clears the terminal screen."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux (and some other Unix-like systems)
    else:
        _ = os.system('clear')
crear_separador = lambda char, length: print(char * length)
nombre_tienda = "FLORERIA JUANITA"
informar_descuento = lambda: print("Nuestra oferta del dia de hoy es: por la compra superior a los $50 te llevas un descuento del 10%")
dar_bienvenida = lambda nombre_tienda: print("Bienvenido a ", nombre_tienda)
preguntar_nombre = lambda: input("Ingrese su nombre: ")
preguntar_compra = lambda: input("Desea comprar flores? (si/no): ").lower()
preguntar_tipo_flor = lambda: input("Ingrese el tipo de flor que desea 1, 2, 3: ")


florOrquidea = "Orquideas"
florTulipan = "Tulipanes"
florGirasol = "Girasoles"
precioOrquidea = 20.0
precioTulipan = 15.0
precioGirasol = 10.0

def imprimir_menu_flores():
    crear_separador("=", 40)
    print("Menu de flores:")
    crear_separador("-", 40)
    print("1. Orquideas - $20.0")
    print("2. Tulipanes - $15.0")
    print("3. Girasoles - $10.0")
    print("4. Finalizar compra")
    crear_separador("-", 40)


#bienvenida
crear_separador("-", 40)
dar_bienvenida(nombre_tienda)
crear_separador("=", 40)

#preguntar nombre
nombre_cliente = preguntar_nombre()
crear_separador("-", 40)

carrito_compras = []
#preguntar si desea comprar flores
desea_comprar = preguntar_compra()

if desea_comprar == "si":
    crear_separador("-", 40)
    print("Excelente ", nombre_cliente, ", tenemos las siguientes flores disponibles:")
    crear_separador("-", 40)    
 
    tipo_flor = 0
    flor_elegida = 0
    total = 0.0
    def calcular_total(carrito):
        suma = 0.0
        for precio in carrito:
            suma += precio
        return suma
    while flor_elegida != 4:
        clear_terminal
        imprimir_menu_flores()
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
            crear_separador("-", 40)
            print("Has elegido la flor tipo ", flor_elegida, " con un precio de $", precio_flor)
            carrito_compras.append(precio_flor)
            print("Flor agregada al carrito.")
            print("Total parcial: $", calcular_total(carrito_compras))
        if flor_elegida == 0:
            print("Por favor, elija una opcion valida.")
    clear_terminal
    if len(carrito_compras) > 0:
        total = calcular_total(carrito_compras)
        crear_separador("=", 40)
        print("El total de su compra es: $", total)
        if total > 50:
            descuento = total * 0.10
            total_con_descuento = total - descuento
            print("Felicidades! Su compra supera los $50, por lo que recibe un descuento del 10%: -$", descuento)
            print("Total con descuento: $", total_con_descuento)
        else:
            print("Su compra no supera los $50, no aplica descuento.")

        crear_separador("-", 40)
        print("Gracias por su compra, ", nombre_cliente, ". Vuelva pronto!")
else:
    print("Gracias por visitarnos, ", nombre_cliente, ". Vuelva pronto!")
    