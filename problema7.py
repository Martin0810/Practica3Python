import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Cuadrante I"
        elif self.x < 0 and self.y > 0:
            return "Cuadrante II"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante III"
        elif self.x > 0 and self.y < 0:
            return "Cuadrante IV"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "Sobre el origen"

    def vector(self, otro_punto):
        vector_resultante = (otro_punto.x - self.x, otro_punto.y - self.y)
        return vector_resultante

    def distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)
        return distancia

class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        return self.base() * self.altura()

def main():
    punto1 = Punto(2, 3)
    punto2 = Punto(5, 7)

    print(f"Punto 1: {punto1}, Cuadrante: {punto1.cuadrante()}")
    print(f"Punto 2: {punto2}, Cuadrante: {punto2.cuadrante()}")

    vector_resultante = punto1.vector(punto2)
    print(f"Vector entre Punto 1 y Punto 2: {vector_resultante}")

    distancia_entre_puntos = punto1.distancia(punto2)
    print(f"Distancia entre Punto 1 y Punto 2: {distancia_entre_puntos:.2f}")

    rectangulo = Rectangulo(punto1, punto2)

    print("\nInformación del Rectángulo:")
    print(f"Base: {rectangulo.base()}")
    print(f"Altura: {rectangulo.altura()}")
    print(f"Área: {rectangulo.area()}")

if __name__ == "__main__":
    main()