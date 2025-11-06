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
    """Imprime una línea separadora."""
    print()
    print(separador * longitud)
    print()

def encontrar_max_longitud_en_arreglo(arreglo):
    """Encuentra la longitud de la cadena más larga en una lista."""
    # Una forma más "Pythónica" de hacer esto sería: return max(len(s) for s in arreglo)
    longitud_maxima = len(arreglo[0])
    for i in range(1, len(arreglo)):
        if longitud_maxima < len(arreglo[i]):
            longitud_maxima = len(arreglo[i])
    return longitud_maxima

def centrar_texto(texto, ancho):
    """Imprime texto centrado en la consola."""
    # Python tiene una función incorporada para esto: texto.center(ancho)
    margen = ancho - len(texto)
    espacios = " " * (margen // 2)
    print(espacios + texto)

#================================================================
# FUNCIONES DE LA FASE 1: ENTRADA A LA DISCOTECA
#================================================================

def preguntar_nombre():
    """Pregunta y devuelve el nombre del cliente."""
    respuesta = ""
    print("Ingresa tu nombre:")
    while len(respuesta) == 0:
        respuesta = input()
        if len(respuesta) > 0:
            nombre_cliente = respuesta
            time.sleep(1)
            limpiar_pantalla()
            return nombre_cliente

def dar_bienvenida(nombre_discoteca, longitud_separador):
    """Imprime el banner de bienvenida."""
    crear_separador("*", longitud_separador)
    centrar_texto(nombre_discoteca, longitud_separador)
    crear_separador("*", longitud_separador)

def validar_edad(frases_entrada):
    """Valida si el cliente es mayor de edad."""
    frase_aleatoria = random.choice(frases_entrada)
    print(frase_aleatoria)
    try:
        edad = int(input())
        if edad < 18:
            print("¡Solo se permiten mayores de edad!")
            es_mayor_de_edad = False
        else:
            es_mayor_de_edad = True
    except ValueError:
        print("Eso no parece una edad válida. Asumiremos que no eres mayor de edad.")
        es_mayor_de_edad = False
        
    limpiar_pantalla()
    return es_mayor_de_edad

def cobrar_entrada(precio_entrada):
    """Pregunta al cliente si desea pagar la entrada."""
    print(f"Perfecto. La entrada cuesta ${precio_entrada}...")
    print("¿Deseas pagar? (Escribe si o no)")
    respuesta = input().lower()
    
    limpiar_pantalla()
    while respuesta not in ["si", "no"]:
        print("Oh discúlpame, pero no te entendí. ¿Deseas pagar? (Escribe si o no)")
        respuesta = input().lower()
        limpiar_pantalla()

    if respuesta == "si":
        print("¡Genial! Aquí tienes tu pulsera...")
        quiere_pagar = True
        time.sleep(2)
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
    print(f" - Crédito restante: ${credito}")
    print(f" - Bebidas consumidas: {bebidas_consumidas}/3")
    crear_separador("=", 50)
    print("¿Qué quieres hacer ahora?\n")
    print("1. Comprar una bebida")
    print("2. Bailar en la pista")
    print("3. Intentar ligar en la barra")
    print("4. Irse a casa")
    
    try:
        accion = int(input())
    except ValueError:
        accion = 0 # Opción inválida
        
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
        # Nota: En Python los arrays (listas) empiezan en el índice 0
        for i in range(len(nombres_bebidas)):
            print(f"{i + 1}. {nombres_bebidas[i]} (${precios_bebidas[i]})")
        print