import random as rd
import sys

numero = rd.randint(0,100)

MIN = 0
MAX = 99

minimo = MIN
maximo = MAX

def pedirNumero(invitacion):
    invitacion += " entre " + str(minimo) + " y " + str(maximo) + ": "
    
    while True:
        entrada =  input(invitacion)
        try:
            entrada = int(entrada)
        except:
            print("Solo introduce numeros del 0 -> 99!!!",file=sys.stderr)
        else:
            if MIN <= entrada <= MAX:
                break 

    return entrada


while True:
    intento = pedirNumero("Adivine el numero")
    if intento<numero:
        print("Demasiado pequenio")
        minimo = intento+1
    elif intento>numero:
        print("Demasiado grande")
        maximo = intento-1
    else:
        print("!Ha ganado¡")
        break
    
