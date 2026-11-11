# Proyecto: Menú Interactivo Modificable


def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Saludar")
    print("2. Sumar dos números")
    print("3. Restar dos números")
    print("4. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            nombre = input("¿Cuál es tu nombre? ")
            print(f"¡Hola, {nombre}! Bienvenido a tu proyecto.")
        elif opcion == "2":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(f"La suma es: {num1 + num2}")
        elif opcion == "3":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(f"La resta es: {num1 - num2}")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()