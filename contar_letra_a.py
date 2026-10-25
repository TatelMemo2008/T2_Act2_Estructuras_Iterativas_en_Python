"""
Programa: Contar letras a
Autor: Ángel Guillermo Andrade Palacios
Fecha: 25 de octubre de 2026
Descripción: Pide una palabra y cuenta cuántas veces aparece la
letra a (mayúscula o minúscula).
"""
 
if __name__ == "__main__":
    # Entrada de datos
    palabra = input("Escribe una palabra: ")
 
    # Proceso
    contador = 0
    for letra in palabra:
        if letra == "a" or letra == "A":
            contador += 1
 
    # Salida
    print(f"La palabra {palabra} tiene {contador} letra(s) a")