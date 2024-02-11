import operaciones

if __name__ == "__main__":
    resultado_suma = operaciones.suma(5, 3)
    print(f"Suma: {resultado_suma}")

    resultado_resta = operaciones.resta(8, 2)
    print(f"Resta: {resultado_resta}")

    resultado_producto = operaciones.producto(4, 6)
    print(f"Producto: {resultado_producto}")

    resultado_division = operaciones.division(9, 3)
    print(f"División: {resultado_division}")

    resultado_error_tipo = operaciones.suma(5, "a")
    print(f"Suma con error de tipo: {resultado_error_tipo}")

    resultado_error_division_cero = operaciones.division(10, 0)
    print(f"División con error de cero: {resultado_error_division_cero}")