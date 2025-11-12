import os
import time
import random
import platform

#================================================================
# FUNCIONES DE UTILIDAD Y CONFIGURACIÓN
#================================================================

def limpiar_pantalla():
    """Limpia la pantalla de la consola, compatible con Windows, Mac y Linux."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def crear_separador(separador, longitud):
    """Imprime una línea separadora con saltos de línea antes y después."""
    print()
    print(separador * longitud)
    print()

def centrar_texto(texto, ancho):
    """Imprime texto centrado en la consola."""
    print(texto.center(ancho))

#================================================================
# FUNCIONES DE LA FASE 1: ENTRADA A LA DISCOTECA
#================================================================

def preguntar_nombre():
    """Pregunta y devuelve el nombre del cliente, asegurando que no esté vacío."""
    respuesta = ""
    print("Ingresa tu nombre:")
    while not respuesta.strip(): # Bucle hasta que se ingrese algo más que espacios
        respuesta = input()
    time.sleep(1)
    limpiar_pantalla()
    return respuesta.strip()

def dar_bienvenida(nombre_discoteca, longitud_separador):
    """Imprime el banner de bienvenida."""
    crear_separador("*", longitud_separador)
    centrar_texto(nombre_discoteca, longitud_separador)
    crear_separador("*", longitud_separador)

def validar_edad(frases_entrada):
    """Valida si el cliente es mayor de edad. Maneja entradas no numéricas."""
    print(random.choice(frases_entrada))
    while True:
        try:
            edad_str = input()
            if not edad_str: continue # Ignorar entrada vacía
            edad = int(edad_str)
            if edad < 18:
                print("¡Solo se permiten mayores de edad!")
                es_mayor_de_edad = False
            else:
                es_mayor_de_edad = True
            limpiar_pantalla()
            return es_mayor_de_edad
        except ValueError:
            print("Eso no parece una edad válida. Por favor, introduce un número.")

def cobrar_entrada(precio_entrada):
    """Pregunta al cliente si desea pagar la entrada."""
    print(f"Perfecto. La entrada cuesta ${precio_entrada:.2f}...")
    print("¿Deseas pagar? (Escribe si o no)")
    
    respuesta = ""
    while respuesta not in ["si", "no"]:
        respuesta = input().lower().strip()
        if respuesta not in ["si", "no"]:
            limpiar_pantalla()
            print("Oh discúlpame, pero no te entendí. ¿Deseas pagar? (Escribe si o no)")

    limpiar_pantalla()
    if respuesta == "si":
        print("¡Genial! Aquí tienes tu pulsera...")
        quiere_pagar = True
    else:
        print("Es una lástima. Que tengas una buena noche...")
        quiere_pagar = False
        
    time.sleep(2)
    limpiar_pantalla()
    return quiere_pagar

#================================================================
# FUNCIONES DE LA FASE 2: DENTRO DE LA DISCOTECA
#================================================================

def preguntar_accion(credito, bebidas_consumidas):
    """Muestra el estado actual y pregunta al jugador qué hacer."""
    print()
    crear_separador("=", 50)
    centrar_texto("Tu estado actual:", 50)
    crear_separador("-", 50)
    print("Estás en la pista. La música suena genial *_*")
    print(f" - Crédito restante: ${credito:.2f}")
    print(f" - Bebidas consumidas: {bebidas_consumidas}/3")
    crear_separador("=", 50)
    print("¿Qué quieres hacer ahora?\n")
    print("1. Comprar una bebida")
    print("2. Bailar en la pista")
    print("3. Intentar ligar en la barra")
    print("4. Irse a casa")
    
    try:
        accion = int(input())
    except (ValueError, EOFError):
        accion = 0 # Opción inválida por defecto
        
    time.sleep(1)
    limpiar_pantalla()
    return accion

def comprar_bebida(credito_actual, bebidas_actuales, nombres_bebidas, precios_bebidas):
    """Maneja la lógica de la compra de bebidas."""
    opcion_comprada = 0  # 0 significa que no se compró nada
    
    if bebidas_actuales >= 3:
        print("Ya has bebido suficiente por esta noche (límite de 3). ¡No seas lámpara!")
    else:
        crear_separador("-_", 25)
        centrar_texto("\\o/ MENU DE TRAGUITOS \\o/", 50)
        crear_separador("_", 50)
        print("¿Qué bebida quieres?\n")
        
        for i, nombre in enumerate(nombres_bebidas):
            print(f"{i + 1}. {nombre} (${precios_bebidas[i]:.2f})")
        print(f"{len(nombres_bebidas) + 1}. Mejor no, volver al menú")
        
        try:
            opcion_bebida = int(input())
            limpiar_pantalla()

            if 1 <= opcion_bebida <= len(nombres_bebidas):
                indice_bebida = opcion_bebida - 1
                if credito_actual >= precios_bebidas[indice_bebida]:
                    print(f"¡Salud! Disfrutas de tu {nombres_bebidas[indice_bebida]}. Te sientes genial.")
                    opcion_comprada = opcion_bebida
                else:
                    print("No tienes suficiente crédito para esa bebida. ¡Qué chiro!")
            else:
                print("Decides no comprar nada por ahora...")
        except (ValueError, EOFError):
            limpiar_pantalla()
            print("Entrada no válida. Decides no comprar nada por ahora...")

    time.sleep(3)
    limpiar_pantalla()
    return opcion_comprada

def animar_baile():
    """Muestra una simple animación de baile en la consola."""
    frames = [
        "  .`+.´.`+.´    (>`-`)>    .+´.`.+´.`  ",
        "  .´ .`+.´ .`+    <(´_´<)    .`.´+.`.´+  ",
        "  .`+.´.`+.´   ^(*_*)\\-    .+´.`.+´.`  ",
        "  .´ .`+.´ .`+    \\m/(-_-)\\m/    . `.´+.`.´+  ",
        "  .`+.´.`+.´    <( `-`)>    .+´.`.+´.`  ",
        "  .´ .`+.´ .`+    \\_( .``)>    . `.´+.`.´+  ",
        "  .`+.´.`+.´    <( ._.)-`    .+´.`.+´.`  "
    ]
    for _ in range(2):
        for frame in frames:
            limpiar_pantalla()
            crear_separador("-_", 50)
            centrar_texto(frame, 100)
            crear_separador("-_", 50)
            time.sleep(0.4)
    limpiar_pantalla()

def accion_bailar():
    """Ejecuta la acción de bailar con un mensaje aleatorio y una animación."""
    frases = [
        "¡Te lanzas a la pista y sacas los pasos prohibidos! La gente alucina.",
        "Justo suena un temazo. ¡Bailas con una energía increíble y todos te hacen espacio!",
        "Intentas un paso de baile nuevo, te tropiezas, pero lo conviertes en un movimiento cool. ¡Nadie se dio cuenta!"
    ]
    print(random.choice(frases))
    time.sleep(3)
    animar_baile()

def accion_ligar():
    """Ejecuta la acción de ligar con un mensaje aleatorio."""
    frases = [
        "Te acercas con tu mejor labia... ¡y funciona! Te da su número. ¡Éxito total!",
        "La persona te sonríe, pero te dice: solo salí a bailar con mis panas. Bueno, se intentó.",
        "La conversación es increíble. No consigues su número, pero te ríes un montón y te sube el ánimo.",
        "La música está tan alta que no se oyen. Terminan haciendo señas y riendo. Fue raro, pero divertido."
    ]
    limpiar_pantalla()
    print(random.choice(frases))
    time.sleep(5)
    limpiar_pantalla()

#================================================================
# SUBPROCESO PARA LA FACTURA
#================================================================
def generar_factura(registro, nombres, precios, costo_entrada):
    """Genera e imprime la factura final de la noche."""
    limpiar_pantalla()
    print()
    crear_separador("=", 50)
    centrar_texto("RESUMEN DE TU NOCHE EN DISCO SIGMA", 50)
    crear_separador("=", 50)
    print("DETALLE DE CONSUMO:\n")
    
    total_factura = costo_entrada
    print(f" - Entrada General ................. ${costo_entrada:.2f}")
    
    if registro:
        for opcion_bebida in registro:
            indice = opcion_bebida - 1
            nombre_bebida = nombres[indice]
            precio_bebida = precios[indice]
            
            linea = f" - {nombre_bebida}"
            print(f"{linea.ljust(35, '.')} ${precio_bebida:.2f}")
            total_factura += precio_bebida
    else:
        print(" (No consumiste ninguna bebida en la barra)")
    
    print()
    crear_separador("-", 50)
    print(f" TOTAL GASTADO: ${total_factura:.2f}")
    crear_separador("=", 50)
    
#================================================================
# ALGORITMO PRINCIPAL
#================================================================
def main():
    """Función principal que ejecuta el simulador de la discoteca."""
    nombre_discoteca = " *_*_ DISCO SIGMA *_*_"
    precio_entrada = 10.0
    
    nombre_cliente = preguntar_nombre()
    
    frases_entrada = [
        f"¡Qué más mi pana {nombre_cliente}! Cédula en mano! ¿Cuántos años tienes?.",
        f"¡La noche está bacansisima! A ver, ¿cuántos años tienes, {nombre_cliente}?.",
        f"¡Ponte once brother! Dime tu edad, {nombre_cliente}.",
        f"¡Chévere que vengas mi pex! A ver esa identificación. ¿Cuál es tu edad, {nombre_cliente}?.",
        f"¿Qué fue, {nombre_cliente}? Muéstrame la cédula, de una. Dime tu edad."
    ]
    
    longitud_separador = max(len(s) for s in frases_entrada)
    dar_bienvenida(nombre_discoteca, longitud_separador)
    
    es_mayor = validar_edad(frases_entrada)
    quiere_pagar = False
    
    if es_mayor:
        print(f"Bienvenido a {nombre_discoteca}")
        crear_separador("-_", 25)
        quiere_pagar = cobrar_entrada(precio_entrada)
    
    if es_mayor and quiere_pagar:
        credito = 21.0
        bebidas_consumidas = 0
        acciones_restantes = 4
        fin_del_programa = False
        registro_de_compras = []
        
        nombres_bebidas = ["Cerveza", "Cuba Libre", "Whisky"]
        precios_bebidas = [3.00, 5.00, 8.00]
        
        while not fin_del_programa:
            accion = preguntar_accion(credito, bebidas_consumidas)
            acciones_restantes -= 1
            
            if accion == 1:
                opcion = comprar_bebida(credito, bebidas_consumidas, nombres_bebidas, precios_bebidas)
                if opcion > 0:
                    costo = precios_bebidas[opcion - 1]
                    credito -= costo
                    bebidas_consumidas += 1
                    registro_de_compras.append(opcion)
                else:
                    acciones_restantes += 1 # No gasta acción si no compra
            elif accion == 2:
                accion_bailar()
            elif accion == 3:
                accion_ligar()
            elif accion == 4:
                print("Decides que ya fue suficiente. ¡Una retirada a tiempo es una victoria!")
                fin_del_programa = True
            else:
                print("Opción inválida. Te quedas un momento pensando qué hacer.")
                acciones_restantes += 1 # No gasta acción si la opción es inválida

            # Comprobar condiciones de fin de noche
            if bebidas_consumidas >= 3 and not fin_del_programa:
                crear_separador("-", 50)
                print("Has llegado a tu límite de 3 bebidas. La noche ha sido buena, pero es hora de irse.")
                fin_del_programa = True
                time.sleep(4)
                
            if acciones_restantes <= 0 and not fin_del_programa:
                limpiar_pantalla()
                crear_separador("-", 50)
                print("De repente, las luces se encienden un poco. El DJ anuncia la última canción.")
                print("¡El tiempo voló! La discoteca va a cerrar. ¡Qué buena farra!")
                fin_del_programa = True
                time.sleep(5)
        
        generar_factura(registro_de_compras, nombres_bebidas, precios_bebidas, precio_entrada)

    # Mensaje Final (se muestra siempre)
    print()
    crear_separador("*", 50)
    centrar_texto(f"GRACIAS POR VENIR, {nombre_cliente.upper()}. ¡HASTA LA PRÓXIMA!", 60)
    crear_separador("*", 50)

# Punto de entrada para ejecutar el programa
if __name__ == "__main__":
    main()