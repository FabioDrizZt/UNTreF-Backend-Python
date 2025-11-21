# Crear un diccionario
producto = {
    'nombre': 'iPhone',
    'precio': 1000.52,
    'stock': 15,
    'wifi': True,
    'infrarrojo': False    
}

# Acceso a los datos

print(producto['nombre'])
print(producto['precio'])

# Modificar los datos
producto['nombre'] = 'iPhone 11'
producto['precio'] = 1000.52
producto['stock'] = 15
producto['wifi'] = True
producto['infrarrojo'] = False

""" del permite borrar una variable o un elemento del diccionario 
edad = 32
del edad
print(edad) """
# borrar un elemento
del producto['infrarrojo']

# Imprimir el diccionario completo
print(producto)

# Acceder a las claves, valores y pares clave-valor
print(producto.keys())
print(producto.values())
print(producto.items())

for clave, valor in producto.items():
    print(f'{clave}: {valor}')