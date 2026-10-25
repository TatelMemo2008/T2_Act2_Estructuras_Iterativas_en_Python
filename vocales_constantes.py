"""
Programa: Vocales o consonantes
Autor: Ángel Guillermo Andrade Palacios
Fecha: 25 de octubre de 2026
Descripción: Pide letras una por una y dice si cada una es vocal o
consonante. Termina cuando se escribe un espacio.
"""
 
# Constantes
VOCALES = "aeiouáéíóúAEIOUÁÉÍÓÚ"
CONSONANTES = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
 
if __name__ == "__main__":
    print("Escribe una letra y pulsa Enter (un espacio para terminar)")
    letra = input("Letra: ")
 
    while letra != " ":
        if len(letra) != 1:
            print("Escribe solo una letra")
        elif letra in VOCALES:
            print(f"{letra} es una vocal")
        elif letra in CONSONANTES:
            print(f"{letra} es una consonante")
        else:
            print(f"{letra} no es una letra")
 
        letra = input("Letra: ")
 
    print("Fin del programa")