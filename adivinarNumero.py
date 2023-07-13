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


numero = pedirNumero("Adivine el numero")

print(numero)
    
