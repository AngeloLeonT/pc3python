class Producto:
    def __init__(self, nombre, marca, modelo, año, categoria):
        self.nombre = nombre
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.categoria = categoria

    def __str__(self):
        return f"{self.nombre} - {self.marca} {self.modelo} ({self.año}), Categoría: {self.categoria}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("El catálogo está vacío.")
        else:
            print("Catálogo de productos:")
            for producto in self.productos:
                print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if productos_filtrados:
            print(f"Productos del año {año}:")
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No hay productos del año {año} en el catálogo.")

    def filtrar_por_categoria(self, categoria):
        productos_filtrados = [producto for producto in self.productos if producto.categoria == categoria]
        if productos_filtrados:
            print(f"Productos de la categoría '{categoria}':")
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No hay productos de la categoría '{categoria}' en el catálogo.")
