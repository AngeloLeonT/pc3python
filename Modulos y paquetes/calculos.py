import operaciones

def main():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        resultado_suma = operaciones.suma(a, b)
        print(f"Suma: {resultado_suma}")

        resultado_resta = operaciones.resta(a, b)
        print(f"Resta: {resultado_resta}")

        resultado_producto = operaciones.producto(a, b)
        print(f"Producto: {resultado_producto}")

        resultado_division = operaciones.division(a, b)
        print(f"División: {resultado_division}")

    except ValueError as ve:
        print(ve)
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"Error inesperado: {e}. Intente nuevamente.")

if __name__ == "__main__":
    main()