"""
Programa: Factorial de un número
Autor: Ángel Guillermo Andrade Palacios
Fecha: 25 de octubre de 2026
Descripción: Pide un número entero y calcula su factorial
multiplicando del 1 hasta ese número.
"""
 
if __name__ == "__main__":
    # Entrada de datos
    n = int(input("Escribe un número entero: "))
 
    if n < 0:
        print("El factorial no existe para números negativos")
    else:
        # Proceso: empiezo en 1 porque 0! también vale 1
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
 
        # Salida
        print(f"El factorial de {n} es {factorial}")