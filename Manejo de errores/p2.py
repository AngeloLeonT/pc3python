def obtener_calificaciones():
    while True:
        try:
            calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")
            calificaciones_lista = calificaciones_str.split(',')
            calificaciones_enteros = [int(cal) for cal in calificaciones_lista]
            return calificaciones_enteros
        except ValueError:
            print("Error: Asegúrese de ingresar valores numéricos correctamente. Intente nuevamente.")

def main():
    try:
        calificaciones = obtener_calificaciones()
        print("Calificaciones ingresadas:", calificaciones)
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"Error inesperado: {e}. Intente nuevamente.")

if __name__ == "__main__":
    main()