import generador_numeros

if __name__ == "__main__":
    lista_aleatoria = generador_numeros.generar_numeros()
    generador_numeros.mostrar_lista(lista_aleatoria)
    generador_numeros.ordenar_y_mostrar(lista_aleatoria)