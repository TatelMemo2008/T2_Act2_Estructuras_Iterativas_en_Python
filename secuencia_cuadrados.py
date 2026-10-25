"""
Programa: Cuadrados
Autor: Ángel Guillermo Andrade Palacios
Fecha: 25 de octubre de 2026
Descripción: Muestra el cuadrado de cada número desde 1 hasta el
número que escriba el usuario. Usa un do-while simulado.
"""
 
if __name__ == "__main__":
    # Entrada de datos
    limite = 0
    while limite < 1:
        limite = int(input("Escribe un número entero positivo: "))
        if limite < 1:
            print("Tiene que ser mayor que 0")
 
    # Do-while simulado
    i = 1
    while True:
        print(f"{i} al cuadrado es {i ** 2}")
        i += 1
        if i > limite:
            break