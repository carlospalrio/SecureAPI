# Se asigna el valor especial 'NaN' (Not a Number) a la variable foo
foo = float('NaN')

# Valor de foo y su tipo de dato 
print(f"foo={foo} type = {type(foo)}")

# Condiciones lógicas
print(
    foo == float("NaN")      # ❌ False: NaN nunca es igual a ningún valor, ni siquiera a otro NaN
    or foo is float("NaN")   # ❌ False: crea un nuevo objeto NaN, diferente al anterior
    or foo < 3               # ❌ False: cualquier comparación con NaN es siempre falsa
    or foo == foo            # ❌ False: NaN no es igual a sí mismo
    or foo is None           # ❌ False: foo es un float, no es None
)
