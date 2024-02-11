import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio**2
        return area

def main():
    radio_circulo = float(input("Ingrese el radio del círculo: "))
    mi_circulo = Circulo(radio_circulo)

    area_circulo = mi_circulo.calcular_area()
    print(f"El área del círculo con radio {mi_circulo.radio} es: {area_circulo:.2f}")

if __name__ == "__main__":
    main()