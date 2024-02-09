import p8

def main():
    numeros_aleatorios = p8.generar_numeros_aleatorios()

    p8.mostrar_lista(numeros_aleatorios)

    p8.ordenar_y_mostrar(numeros_aleatorios)

if __name__ == "__main__":
    main()