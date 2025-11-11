# Convertir tipos de datos a cadenas

numero = 100
print(str(numero) + " es un numero")
lista = [1, 2, 3] # o tupla, diccionario, etc.
print(str(lista) + " es una lista")

# Convertir tipos de datos a enteros
""" inputsNumericos = "100"
print(int(inputsNumericos)-50)
año_nacimiento = input('Ingrese su año de nacimiento: ') # Ej: "1990"
edad = 2025 - int(año_nacimiento)
print(edad) """

# Convertir tipos de datos a flotantes
inputsNumericos = "100.75"
print(float(inputsNumericos)-50.25)

# Convertir tipos de datos a booleanos
print(bool(0))     # False
print(bool(0.0000))     # False
print(bool(0j))     # False
print(bool(0+0j))     # False
print(bool(""))     # False
print(bool([]))  # False
print(bool(None))  # False
print(bool({}))  # False
print(bool(())) # False
print(bool(set())) # False

print(bool(" "))     # True
print(bool([1, 2, 3]))  # True
print(bool({"key": "value"}))  # True
print(bool(-5))    # True
print(bool(1))     # True