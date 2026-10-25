"""
Programa: Media de números positivos
Autor: Ángel Guillermo Andrade Palacios
Fecha: 25 de octubre de 2026
Descripción: Pide números uno por uno y termina cuando se escribe un
número negativo. Al final muestra la media de los positivos.
"""
 
if __name__ == "__main__":
    suma = 0
    contador = 0
 
    print("Escribe números positivos (con uno negativo se termina)")
    numero = float(input("Número: "))
 
    while numero >= 0:
        # El cero no es positivo, así que no lo cuento
        if numero > 0:
            suma += numero
            contador += 1
        numero = float(input("Número: "))
 
    # Si no hubo positivos no se puede dividir entre 0
    if contador == 0:
        print("No escribiste ningún número positivo")
    else:
        media = suma / contador
        print(f"La media de los {contador} números positivos es: {media:.2f}")