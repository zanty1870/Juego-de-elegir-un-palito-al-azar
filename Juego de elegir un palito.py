from random import *

# lista inicial
palitos = ["-","--","---","----"]


# mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

# pedir intento
def probar_suerte():
    intento = " "

    while intento not in ["1","2","3","4"]:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)

# comprobar intento

def comprobar_intento(lista,intento):
    if lista[intento -1] == "-":
        print("perdiste")

    else:
        print("Ganaste")

    print(f"Te toco {lista[intento-1]}")

palitos_mezclados = mezclar(palitos)
eleccion = probar_suerte()
comprobar_intento(palitos_mezclados,eleccion)