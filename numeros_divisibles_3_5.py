"""
Programa: Divisibles entre 3 y 5
Autor: Ángel Guillermo Andrade Palacios
Fecha: 25 de octubre de 2026
Descripción: Imprime los números del 1 al 100 que se pueden dividir
entre 3 y entre 5 al mismo tiempo.
"""
 
if __name__ == "__main__":
    print("Números del 1 al 100 divisibles entre 3 y 5:")
 
    # Un número es divisible si el residuo de la división es 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=" ")
 
    print()