def limpiar():
  import os
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

# crear una lista heterogénea
datos = [23, "Hola", 3.14, True, [1, 2, 3], ('AR', 'BR', 'CL'), {"clave": "valor"}]
#        int   str   float bool    list      tuple              dict
print(datos)

def mostrar_lista(lista):
  # primer elemento: Argentina
  print(f"Primer elemento: {lista[0]}")
  # ultimo elemento: Paraguay
  print(f"Último elemento: {lista[-1]}")
  # elemento en la posición 2
  print(f"Elemento en la posición 2: {lista[2]}")
  # elemento en la posición -2
  print(f"Elemento en la posición -2: {lista[-2]}")
  # elemento en la posición 4
  print(f"Elemento en la posición 4: {lista[4]}")
  # elemento en la posición -4
  print(f"Elemento en la posición -4: {lista[-4]}")
   # elemento en la posición -5
  print(f"Elemento en la posición -5: {lista[-5]}")
  # elemento en la posición 5
  try:
    print(f"Elemento en la posición 5: {lista[5]}")
  except IndexError:
    print("No hay elemento en la posición 5")
  
# crear una lista homogénea
paises = ["Argentina", "Brasil", "Chile", "Uruguay", "Paraguay"]
# indice  0             1         2       3          4
# indices negativos -5        -4        -3      -2         -1
mostrar_lista(paises) 
print(f"los paises cargados son {paises}")
limpiar()

def mostrar_sub_lista(lista, inicio=0, fin=None):
  if fin is None:
    fin = len(lista)
  print(f"Sub lista desde {inicio} hasta {fin}: {lista[inicio:fin]}")

print(f"La lista tiene {len(paises)} elementos.")
mostrar_sub_lista(paises)          # toda la lista
mostrar_sub_lista(paises, 1)       # desde el índice 1 hasta el final
mostrar_sub_lista(paises, 0, 2)    # desde el índice 0 hasta el índice 2
mostrar_sub_lista(paises, 2, 4)    # desde el índice 2 hasta el índice 4
mostrar_sub_lista(paises, -2, -1)  # desde el índice -2 hasta el índice -1

lista_vacia = []
mostrar_sub_lista(lista_vacia)