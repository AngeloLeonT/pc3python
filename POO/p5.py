class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = None

    def display(self):
        print("Información del estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        else:
            print("Edad: No asignada")
        if self.notas is not None:
            print(f"Notas: {', '.join(map(str, self.notas))}")
        else:
            print("Notas: No asignadas")

    def set_edad(self, edad):
        if edad < 0:
            raise ValueError("Error: La edad no puede ser un valor negativo.")
        self.edad = edad

    def set_notas(self, notas):
        for nota in notas:
            if nota < 0 or nota > 100:
                raise ValueError("Error: Las notas deben estar en el rango de 0 a 100.")
        self.notas = notas