import random as rd
import sys


def pedirNumero(invitacion,minimo,maximo):
    invitacion += " entre " + str(minimo) + " y " + str(maximo) + ": "
    
    while True:
        entrada =  input(invitacion)
        try:
            entrada = int(entrada)
        except:
            print("Solo introduce numeros del 0 -> 99!!!",file=sys.stderr)
        else:
            if minimo <= entrada <= maximo:
                break 

    return entrada

def evaluarJuego(numero):
    minimo = 0
    maximo = 99
    while True:
        intento = pedirNumero("Adivine el numero",minimo,maximo)
        if intento<numero:
            print("Demasiado pequenio")
            minimo = intento+1
        elif intento>numero:
            print("Demasiado grande")
            maximo = intento-1
        else:
            print("!Ha ganado¡")
            break
    

def jugar():
    numero = rd.randint(0,100)
    evaluarJuego(numero)

jugar()