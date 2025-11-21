from tabulate import tabulate

""" en js las importaciones eran
import tabulate from 'tabulate';
import { funcionalidad } from 'modulo';

en python las importaciones eran
from tabulate import tabulate
from modulo import funcionalidad

"""

encabezado = ["#", "Fruta"]
frutas = ["manzana", "pera", "naranja", "limón", "mango"]

tabla_frutas = [[idx+1, fruta] for idx, fruta in enumerate(frutas)]

""" for idx, fruta in tabla_frutas:
    print(f'{idx+1}. {fruta}') """

print(tabulate(tabla_frutas, headers=encabezado))
""" print(tabulate(tabla_frutas, headers=encabezado, tablefmt="keys")) """
print(tabulate(tabla_frutas, headers=encabezado, tablefmt="html"))
print(tabulate(tabla_frutas, headers=encabezado, tablefmt="grid"))
print(tabulate(tabla_frutas, headers=encabezado, tablefmt="fancy_grid"))
print(tabulate(tabla_frutas, headers=encabezado, tablefmt="github"))
print(tabulate(tabla_frutas, headers=encabezado, tablefmt="latex"))