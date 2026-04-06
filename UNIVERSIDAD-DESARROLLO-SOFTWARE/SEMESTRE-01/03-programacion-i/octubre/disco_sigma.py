import random


def gen_divider(characters, length):
    print(characters * length)


def center_text(text, width):
    margin = int((width - len(text))/2)    
    print(" " * margin + text)


# ================================================================
# PHASE 1 FUNCTIONS: --ENTERING THE CLUB--
# ================================================================
def ask_name():
    name = input("Ingresa tu nombre: ")
    name_lenght = len(name)
    if name_lenght == 0:
        print("¿Por qué tan callado?")
        ask_name()
    elif name_lenght > 50:
        print("Dale suave...")
        ask_name()
    return name


def welcome(club_name):
    width = 130
    gen_divider("*", width)
    center_text(club_name, width)
    gen_divider("*", width)


def ask_age(clients_name):
    WELCOMING_SENTENCES = [
        f"¡Cédula en mano, {clients_name}! ¿Cuántos años tienes?.",
        f"¡La noche está bacansisima! A ver, ¿cuántos años tienes, {clients_name}?.",
        f"¡Ponte once brother! Dime tu edad, {clients_name}",
        f"¡Chévere que vengas mi pex! A ver esa identificación. ¿Cuál es tu edad, {clients_name}?.",
        f"¿Oe, {clients_name}? Muéstrame la cédula, de una. Dime tu edad.",
    ]
    random_index = random.randrange(len(WELCOMING_SENTENCES))
    print(WELCOMING_SENTENCES[random_index])
    age = input()
    if age == '':        
        ask_age(clients_name)
    if int(age) < 0:
        print("Solo se admiten valores positivos")
        ask_age(clients_name)
    elif int(age) > 99:
        print("Jajaja que buena broma, pero ya en serio dime tu edad")
        ask_age(clients_name)
    elif int(age) < 18 :
        print("¡Solo se permiten mayores de edad!")
        return True
    return True

def ask_for_cover(cover) :
    print(f"Perfecto. La entrada cuesta ${cover}...")
    answer = input("¿Deseas pagar? (Escribe si o no) ")
    while True :
        if str(answer).lower == "si" or str(answer).lower == "no":
            break
        print("Oh discúlpame, pero no te entendí. ¿Deseas pagar? (Escribe si o no)")
        answer = input()
    print("")
    if str(answer).lower == "si":
        print("¡Genial! Aquí tienes tu pulsera...")
        return True
    else :
        print("Es una lástima. Que tengas una buena noche...")
        return False


club_name = "DISCO SIGMA"
cover = 10.0
welcome(club_name)
clients_name = ask_name()
under_age = ask_age(clients_name)
is_willing_to_pay = False

if not under_age :
    print(f"Bienvenido a {club_name}")
    gen_divider("-", 25)
    is_willing_to_pay = ask_for_cover(cover)

if is_willing_to_pay :
    credit = 21
    payed_drinks = 0
    is_end_of_program = False
    accion_credits = 4
    
    Drinks = [
        ["Cerveza", 3.00],
        ["Cuba Libre", 5.00],
        ["Whisky", 8.00],
    ]
    
    while not is_end_of_program :
        action = ask_next_action(credit, payed_drinks)
        action_credits -= 1
        
        
            
             
            
