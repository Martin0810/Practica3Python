from circulo import Circulo
from rectangulo import Rectangulo

def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado (funcionalidad no implementada)")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = Circulo(radio)
            area_circulo = circulo.calcular_area()
            print(f"El área del círculo es: {area_circulo}")
        elif opcion == "2":
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            rectangulo = Rectangulo(largo, ancho)
            area_rectangulo = rectangulo.calcular_area()
            print(f"El área del rectángulo es: {area_rectangulo}")
        elif opcion == "3":
            print("Funcionalidad de calcular el área de un cuadrado no implementada.")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

if __name__ == "__main__":
    main()