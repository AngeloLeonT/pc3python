import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        if self.radio < 0:
            raise ValueError("Error: El radio no puede ser un valor negativo.")
        else:
            area = math.pi * (self.radio ** 2)
            return area

# Ejemplo de uso
try:
    radio_circulo = float(input("Ingrese el radio del círculo: "))
    mi_circulo = Circulo(radio_circulo)
    area_del_circulo = mi_circulo.calcular_area()
    print(f"El área del círculo con radio {radio_circulo} es: {area_del_circulo}")
except ValueError as ve:
    print(ve)
except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario.")
except Exception as e:
    print(f"Error inesperado: {e}. Intente nuevamente.")

    