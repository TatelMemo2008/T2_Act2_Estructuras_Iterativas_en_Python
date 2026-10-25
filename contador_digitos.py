"""
Programa: Contador de dígitos
Autor: Ángel Guillermo Andrade Palacios
Fecha: 25 de octubre de 2026
Descripción: Pide un número entero y cuenta cuántos dígitos tiene
dividiéndolo entre 10 hasta que llegue a 0.
"""
 
if __name__ == "__main__":
    # Entrada de datos
    numero = int(input("Escribe un número entero: "))
 
    # Trabajo con una copia positiva para no perder el número original
    copia = numero
    if copia < 0:
        copia = copia * -1
 
    # Proceso
    digitos = 0
    while copia > 0:
        copia = copia // 10
        digitos += 1
 
    # El 0 no entra al ciclo, pero sí tiene un dígito
    if numero == 0:
        digitos = 1
 
    # Salida
    print(f"El número {numero} tiene {digitos} dígito(s)")