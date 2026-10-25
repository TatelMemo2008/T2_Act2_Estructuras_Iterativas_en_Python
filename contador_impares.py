"""
Programa: Números impares
Autor: Ángel Guillermo Andrade Palacios
Fecha: 25 de octubre de 2026
Descripción: Muestra los números impares desde 1 hasta el número que
escriba el usuario. Usa un do-while simulado con while True y break.
"""
 
if __name__ == "__main__":
    # Entrada de datos: repito hasta que el número sea positivo
    limite = 0
    while limite < 1:
        limite = int(input("Escribe un número entero positivo: "))
        if limite < 1:
            print("Tiene que ser mayor que 0")
 
    print(f"Impares del 1 al {limite}:")
 
    # Do-while simulado: el bloque se ejecuta al menos una vez
    impar = 1
    while True:
        print(impar, end=" ")
        impar += 2
        if impar > limite:
            break
 
    print()