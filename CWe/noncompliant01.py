# Función que determina si el valor ingresado representa un balance positivo
def balance_is_positive(value: str) -> bool:

    # Se convierte el valor de texto a un float.
    _value = float(value)

    # Intenta detectar NaN o None
    if _value == float("NaN") or _value is float("NaN") or _value is None:
        raise ValueError("Expected a float")

    # Si el valor es menor o igual a cero, se considera que no hay balance positivo
    if _value <= 0:
        return False
    else:
        return True



# 0.01 → es mayor que cero → retorna True
print(balance_is_positive("0.01"))

# 0.001 → también mayor que cero → retorna True
print(balance_is_positive("0.001"))

# Exception
print(balance_is_positive("NaN"))
