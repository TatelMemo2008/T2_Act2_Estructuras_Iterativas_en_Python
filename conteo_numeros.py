"""
Programa: Conteo de números
Autor: Ángel Guillermo Andrade Palacios
Fecha: 25 de octubre de 2026
Descripción: Pide una cantidad de números y al final dice cuántos
fueron mayores, menores o iguales a cero.
"""
 
if __name__ == "__main__":
    # Entrada de datos: repito la pregunta hasta que la cantidad sea válida
    cantidad = 0
    while cantidad < 1:
        cantidad = int(input("¿Cuántos números vas a escribir? "))
        if cantidad < 1:
            print("La cantidad tiene que ser al menos 1")
 
    # Contadores
    mayores = 0
    menores = 0
    iguales = 0
 
    # Proceso
    for i in range(cantidad):
        numero = float(input(f"Número {i + 1}: "))
        if numero > 0:
            mayores += 1
        elif numero < 0:
            menores += 1
        else:
            iguales += 1
 
    # Salida
    print(f"Mayores que 0: {mayores}")
    print(f"Menores que 0: {menores}")
    print(f"Iguales a 0: {iguales}")