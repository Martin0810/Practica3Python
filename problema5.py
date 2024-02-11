class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Información del estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        print(f"Edad: {self.edad if self.edad is not None else 'No asignada'}")
        print(f"Notas: {', '.join(map(str, self.notas)) if self.notas else 'No asignadas'}")

    def set_edad(self, edad):
        self.edad = edad

    def set_notas(self, notas):
        self.notas = notas

def main():
    nombre_alumno = input("Ingrese el nombre del alumno: ")
    numero_registro_alumno = input("Ingrese el número de registro del alumno: ")
    mi_alumno = Alumno(nombre_alumno, numero_registro_alumno)

    mi_alumno.display()

    edad_alumno = int(input("Ingrese la edad del alumno: "))
    mi_alumno.set_edad(edad_alumno)

    notas_alumno = [float(nota) for nota in input("Ingrese las notas del alumno separadas por coma: ").split(',')]
    mi_alumno.set_notas(notas_alumno)

    mi_alumno.display()

if __name__ == "__main__":
    main()