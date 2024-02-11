class Producto:
    def __init__(self, nombre, precio, año, categoria):
        self.nombre = nombre
        self.precio = precio
        self.año = año
        self.categoria = categoria

    def __str__(self):
        return f"{self.nombre} - ${self.precio} - Año: {self.año} - Categoría: {self.categoria}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_lista(self):
        print("Lista de productos:")
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        return productos_filtrados

    def filtrar_por_categoria(self, categoria):
        productos_filtrados = [producto for producto in self.productos if producto.categoria.lower() == categoria.lower()]
        return productos_filtrados

def main():
    mi_catalogo = Catalogo()

    mi_catalogo.agregar_producto(Producto("Batería", 100, 2022, "Accesorios"))
    mi_catalogo.agregar_producto(Producto("Filtro de aceite", 15, 2021, "Mantenimiento"))
    mi_catalogo.agregar_producto(Producto("Llantas", 200, 2022, "Neumáticos"))

    mi_catalogo.mostrar_lista()

    año_filtro = 2022
    productos_filtrados_por_año = mi_catalogo.filtrar_por_año(año_filtro)
    print(f"\nProductos filtrados por año {año_filtro}:")
    for producto in productos_filtrados_por_año:
        print(producto)

    categoria_filtro = "Mantenimiento"
    productos_filtrados_por_categoria = mi_catalogo.filtrar_por_categoria(categoria_filtro)
    print(f"\nProductos filtrados por categoría {categoria_filtro}:")
    for producto in productos_filtrados_por_categoria:
        print(producto)

if __name__ == "__main__":
    main()