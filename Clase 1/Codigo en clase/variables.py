
mi_nombre = "D'artagnan"
print(mi_nombre)
print(type(mi_nombre))

edad = 25
print(type(edad))

edad = 25.0
print(type(edad))

# Python tiene un tipado fuerte
# No realiza conversiones de tipo automatica

# print(10+"2")
print(f"Mi edad es {edad}")

# f-strings (literal de cadena de formato)
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings

nombre = "D'artagnan"
edad = 25

# console.log(`Mi nombre es ${nombre} y tengo ${edad} años`)
print(f"Mi nombre es {nombre} y tengo {edad} años")

# Asignacion multiple de variables
a, b, c = 1, 2, 3
print(a, b, c)

# intercambio de variables
a, b = b, a
print(a, b)

# En python no existen constantes PERO se pueden crear variables en mayusculas
PI = 3.141592653589793
print(PI)
GRAVEDAD_TIERRA = 9.8
print(GRAVEDAD_TIERRA)

# Variables booleanas
es_malo = True
print(f"Es malo? {es_malo}")
es_malo = False
print(f"Es malo? {es_malo}")
