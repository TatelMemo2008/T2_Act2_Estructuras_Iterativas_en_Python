"""
Programa: Calculadora con menú
Autor: Ángel Guillermo Andrade Palacios
Fecha: 25 de octubre de 2026
Descripción: Calculadora que suma, resta, multiplica y divide. Después
de cada operación pregunta si el usuario quiere continuar.
"""
 
if __name__ == "__main__":
    while True:
        print("\n=== CALCULADORA ===")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        opcion = int(input("Elige una opción: "))
 
        if opcion >= 1 and opcion <= 4:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
 
        match opcion:
            case 1:
                print(f"{num1:g} + {num2:g} = {num1 + num2:g}")
            case 2:
                print(f"{num1:g} - {num2:g} = {num1 - num2:g}")
            case 3:
                print(f"{num1:g} * {num2:g} = {num1 * num2:g}")
            case 4:
                if num2 == 0:
                    print("No se puede dividir entre cero")
                else:
                    print(f"{num1:g} / {num2:g} = {num1 / num2:g}")
            case _:
                print("Opción no válida")
 
        continuar = input("¿Quieres continuar? (s/n): ")
        if continuar != "s" and continuar != "S":
            print("Hasta luego")
            break