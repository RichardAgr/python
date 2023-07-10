import random as rd
import sys

numero = rd.randint(0,100)
numAdivinar = input("Adivine el numero: ")

try:
    numAdivinar = int(numAdivinar)
except:
    print("Error, no ingreso un numero")
    sys.exit()
    
