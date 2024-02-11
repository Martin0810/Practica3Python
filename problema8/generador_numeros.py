import random

def generar_numeros():
    return [random.randint(0, 100) for _ in range(20)]

def mostrar_lista(lista):
    print("Lista de números:")
    print(lista)

def ordenar_y_mostrar(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    print(lista_ordenada)

if __name__ == "__main__":
    lista_aleatoria = generar_numeros()
    mostrar_lista(lista_aleatoria)
    ordenar_y_mostrar(lista_aleatoria)