class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        area = self.largo * self.ancho
        return area

def main():
    largo_rectangulo = float(input("Ingrese el largo del rectángulo: "))
    ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))
    mi_rectangulo = Rectangulo(largo_rectangulo, ancho_rectangulo)

    area_rectangulo = mi_rectangulo.calcular_area()
    print(f"El área del rectángulo con largo {mi_rectangulo.largo} y ancho {mi_rectangulo.ancho} es: {area_rectangulo}")

if __name__ == "__main__":
    main()