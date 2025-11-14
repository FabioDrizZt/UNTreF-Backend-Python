tupla_monedas = ("peso", "dolar", "real", "euro", "yuan")

print(tupla_monedas)
print(tupla_monedas[0])
print(tupla_monedas[1])
print(tupla_monedas[2])
print(tupla_monedas[3])
print(tupla_monedas[4])

# Las tuplas son inmutables, no se pueden modificar
# tupla_monedas[0] = "pesos" # error

estados_peliculas = ("pendiente", "viendo", "terminada", "abandonada")
estados_pedido_rappi = ("pendiente", "en camino", "entregado", "cancelado")
provincias_argentinas = (
  "Buenos Aires",
  "Catamarca",
  "Chaco",
  "Chubut",
  "Corrientes",
  "Entre Rios",
  "Formosa",
  "Jujuy",
  "La Pampa",
  "La Rioja",
  "Mendoza",
  "Misiones",
  "Neuquen",
  "Rio Negro",
  "Salta",
  "San Juan",
  "San Luis",
  "Santa Cruz",
  "Santa Fe",
  "Santiago del Estero",
  "Tierra del Fuego",
  "Tucuman"
)

def mostrar_tupla(tupla):
  # primer elemento: Argentina
  print(f"Primer elemento: {tupla[0]}")
  # ultimo elemento: Paraguay
  print(f"Último elemento: {tupla[-1]}")
  # elemento en la posición 2
  print(f"Elemento en la posición 2: {tupla[2]}")
  # elemento en la posición -2
  print(f"Elemento en la posición -2: {tupla[-2]}")
  # elemento en la posición 4
  print(f"Elemento en la posición 4: {tupla[4]}")
  # elemento en la posición -4
  print(f"Elemento en la posición -4: {tupla[-4]}")
   # elemento en la posición -5
  print(f"Elemento en la posición -5: {tupla[-5]}")
  # elemento en la posición 5
  try:
    print(f"Elemento en la posición 5: {tupla[5]}")
  except IndexError:
    print("No hay elemento en la posición 5")
    
mostrar_tupla(provincias_argentinas)

import os
os.system("cls")

def mostrar_sub_tupla(tupla, inicio=0, fin=None):
  if fin is None:
    fin = len(tupla)
  print(f"Sub tupla desde {inicio} hasta {fin}: {tupla[inicio:fin]}")

print(f"La tupla tiene {len(provincias_argentinas)} elementos.")
mostrar_sub_tupla(provincias_argentinas)          # toda la lista
mostrar_sub_tupla(provincias_argentinas, 1)       # desde el índice 1 hasta el final
mostrar_sub_tupla(provincias_argentinas, 0, 2)    # desde el índice 0 hasta el índice 2
mostrar_sub_tupla(provincias_argentinas, 2, 4)    # desde el índice 2 hasta el índice 4
mostrar_sub_tupla(provincias_argentinas, -2, -1)  # desde el índice -2 hasta el índice -1
mostrar_sub_tupla(provincias_argentinas, -2)  # desde el índice -2 hasta el ultimo