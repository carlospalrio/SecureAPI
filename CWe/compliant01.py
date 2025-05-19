
# Link Video: https://monlaues-my.sharepoint.com/:v:/g/personal/carlospalrio_campus_monlau_com/ERvWxrucskZCkW2ykh2r6mIBed3Nt9VhkI0o4wODqgtk5w?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=ugQCKF





from decimal import ROUND_DOWN, Decimal

# Función que evalúa si un valor numérico representa un balance positivo
def balance_is_positive(value: str) -> bool:

    # Conversión directa de la cadena a Decimal 
    _value = Decimal(value)

    # Redondeo del valor a dos decimales usando ROUND_DOWN y comparación con cero
    return _value.quantize(Decimal(".01"), rounding=ROUND_DOWN) > Decimal("0.00")




# 0.01 es positivo => True
print(balance_is_positive("0.01"))

# 0.001 se redondea a 0.00 => False
print(balance_is_positive("0.001"))

# 'NaN' genera una excepción porque no se puede cuantizar
# Esto detendrá la ejecución del programa si no se maneja la excepción
print(balance_is_positive("NaN"))
