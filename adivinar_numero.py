"""
Programa: Adivinar el número
Autor: Ángel Guillermo Andrade Palacios
Fecha: 25 de octubre de 2026
Descripción: La computadora elige un número del 1 al 100 y el usuario
tiene que adivinarlo. Le dice si se pasó o se quedó corto.
"""
 
import random
 
if __name__ == "__main__":
    numero_secreto = random.randint(1, 100)
    suposicion = 0
    intentos = 0
 
    print("Adivina el número que pensé, está entre 1 y 100")
 
    while suposicion != numero_secreto:
        suposicion = int(input("Tu número: "))
        intentos += 1
 
        if suposicion < numero_secreto:
            print("Muy bajo, intenta con uno más grande")
        elif suposicion > numero_secreto:
            print("Muy alto, intenta con uno más chico")
        else:
            print(f"¡Adivinaste! Era el {numero_secreto}")
            print(f"Lo lograste en {intentos} intento(s)")