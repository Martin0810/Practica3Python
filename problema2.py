def obtener_calificaciones():
    while True:
        entrada = input("Ingrese una lista de calificaciones separadas por comas: ")

        try:
            calificaciones = [int(calificacion.strip()) for calificacion in entrada.split(',')]
            return calificaciones
        except ValueError:
            print("Error: Asegúrese de ingresar valores numéricos separados por comas.")

def main():
    calificaciones = obtener_calificaciones()

    if calificaciones:
        print("Calificaciones ingresadas:")
        for calificacion in calificaciones:
            print(calificacion)

if __name__ == "__main__":
    main()