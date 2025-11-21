from tabulate import tabulate
""" from productos import productos_apple as apple, productos_google as google """
""" from productos import * """
""" import productos """
from productos import productos_apple, productos_google

headers = ["Nombre", "Precio", "Stock", "Wifi"]
tabla_productos = [
    [p["nombre"], p["precio"], p["stock"], p["wifi"]] for p in productos_apple
]

print(tabulate(tabla_productos, headers=headers, tablefmt="fancy_grid"))

tabla_productos = [
    [p["nombre"], p["precio"], p["stock"], p["wifi"]] for p in productos_google
]
print(tabulate(tabla_productos, headers=headers, tablefmt="fancy_grid"))
