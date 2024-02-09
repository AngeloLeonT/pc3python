class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        if self.largo < 0 or self.ancho < 0:
            raise ValueError("Error: El largo y el ancho deben ser valores no negativos.")
        else:
            area = self.largo * self.ancho
            return area

# Ejemplo de uso
try:
    largo_rectangulo = float(input("Ingrese el largo del rectángulo: "))
    ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))
    
    mi_rectangulo = Rectangulo(largo_rectangulo, ancho_rectangulo)
    area_del_rectangulo = mi_rectangulo.calcular_area()
    
    print(f"El área del rectángulo con largo {largo_rectangulo} y ancho {ancho_rectangulo} es: {area_del_rectangulo}")
except ValueError as ve:
    print(ve)
except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario.")
except Exception as e:
    print(f"Error inesperado: {e}. Intente nuevamente.")