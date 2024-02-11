def obtener_porcentaje(fraction):
    try:
        x, y = map(int, fraction.split('/'))

        if x < 0 or y <= 0 or x > y:
            raise ValueError("X y Y deben ser números enteros, X debe ser menor o igual a Y, y Y no puede ser igual a 0.")

        porcentaje = (x / y) * 100

        if porcentaje < 1:
            return 'E'
        elif porcentaje > 99:
            return 'F'
        else:
            return f'{round(porcentaje)}%'

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except ZeroDivisionError:
        print("Error: Y no puede ser igual a 0.")
        return None

def main():
    while True:
        entrada = input("Ingrese una fracción en formato X/Y: ")
        resultado = obtener_porcentaje(entrada)

        if resultado is not None:
            print(f"La cantidad de combustible en el tanque es: {resultado}")
            break

if __name__ == "__main__":
    main()