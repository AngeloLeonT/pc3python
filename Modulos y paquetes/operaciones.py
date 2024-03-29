def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        raise ValueError("Error: Tipo de dato no válido.")

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        raise ValueError("Error: Tipo de dato no válido.")

def producto(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        raise ValueError("Error: Tipo de dato no válido.")

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Error: No es posible dividir entre cero.")
        resultado = a / b
        return resultado
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(str(e))