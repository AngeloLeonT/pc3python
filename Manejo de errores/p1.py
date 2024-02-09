

def obtener_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y (donde X e Y son enteros): ")
            x, y = map(int, fraccion.split('/'))

            if x <= 0 or y <= 0 or x > y:
                raise ValueError("X debe ser menor o igual a Y, y ambos deben ser mayores que 0")

            return x, y
        except ValueError as ve:
            print(f"Error: {ve}. Intente nuevamente.")
        except ZeroDivisionError:
            print("Error: Y no puede ser 0. Intente nuevamente.")

def calcular_porcentaje(x, y):
    porcentaje = (x / y) * 100

    if porcentaje < 1:
        return 'E'
    elif porcentaje > 99:
        return 'F'
    else:
        return f'{round(porcentaje)}%'

def main():
    while True:
        try:
            x, y = obtener_fraccion()
            resultado = calcular_porcentaje(x, y)
            print(f"La cantidad de combustible en el tanque es: {resultado}")
            break
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"Error inesperado: {e}. Intente nuevamente.")

if __name__ == "__main__":
    main()