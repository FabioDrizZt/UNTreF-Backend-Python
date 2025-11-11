""" 
El tipo de dato es el tipo de informacion que se almacena en una variable.
Para poder saber el tipo de dato de una variable se usa el comando type()
"""

print("int:")
print(type(1))
print(type(0))
print(type(-5))
print(type(16516135738765165157575275))

print("float:")
print(type(1.0))
print(type(0.0))
print(type(-5.0))
print(type(16516135738765165157575275.0))
print(type(1e3))

print("complex:")
print(type(1j))
print(type(0j))
print(type(1.0j))
print(type(1 + 1j))

print("bool:")
print(type(True))
print(type(False))
print(type(1 == 1))
print(type(1 < 2))

print("str:")
print(type("Hola"))
print(type('Hola'))
print(type("""Hola"""))

print("NoneType:")
print(type(None))

# Para saber si coincide con un tipo de dato
if type(1) == int:
    print("Es un int")

if isinstance(1, int):
    print("Es un int")
    
print("list:")
lista = [1, 2, 3]
print(type(lista))

print("tuple:")
tupla = (1, 2, 3)
print(type(tupla))

print("dictionary:")
diccionario = {"key": "value"}
diccionario["key2"] = "value2"
print(type(diccionario))

print("set:")
seta = {1, 2, 3}
print(type(seta))

