"""
Programa: Secuencia aritmética
Autor: Ángel Guillermo Andrade Palacios
Fecha: 25 de octubre de 2026
Descripción: Genera una secuencia aritmética a partir del primer
número y la diferencia, sin pasarse del número máximo. Usa un
do-while simulado.
"""
 
if __name__ == "__main__":
    # Entrada de datos
    primero = int(input("Primer número: "))
 
    diferencia = 0
    while diferencia < 1:
        diferencia = int(input("Diferencia: "))
        if diferencia < 1:
            print("La diferencia tiene que ser mayor que 0")
 
    maximo = int(input("Número máximo: "))
 
    if primero > maximo:
        print("El primer número no puede ser mayor que el máximo")
    else:
        # Do-while simulado
        numero = primero
        print("Secuencia:")
        while True:
            print(numero, end=" ")
            numero += diferencia
            if numero > maximo:
                break
        print()