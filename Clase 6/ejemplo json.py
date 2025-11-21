from productos import productos_apple, productos_google
import json

# Guardar en un archivo json
with open("productos.json", "w") as f:
    json.dump(productos_apple, f, indent=4)
# Leer desde un archivo json
with open("productos.json", "r") as f:
    productos_apple = json.load(f)

for idx, producto in enumerate(productos_apple):
    print(f'{idx+1}. {producto["nombre"]}')