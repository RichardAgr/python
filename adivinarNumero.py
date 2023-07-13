import random as rd
import sys


MIN = 0
MAX = 99

def pedirNumero(invitacion):
    invitacion += " entre " + str(MIN) + " y " + str(MAX) + ": "
    
    while True:
        entrada =  input(invitacion)
        try:
            entrada = int(entrada)
        except:
            pass
        else:
            if MIN <= entrada <= MAX:
                break 
    return entrada


numero = rd.randint(0,100)

while True:
    intento = pedirNumero("Adivine el numero")
    if intento<numero:
        print("Demasiado pequenio")
    elif intento>numero:
        print("Demasiado grande")
    else:
        print("!Ha ganado¡")
        break
    
