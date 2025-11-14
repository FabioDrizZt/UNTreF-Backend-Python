# index devuelve el índice de un elemento

def mostrar_indice(lista, elemento):
  try:
    print(f"El índice del elemento {elemento} es {lista.index(elemento)}")
  except ValueError:
    print(f"No se puede encontrar el elemento {elemento}")
  except Exception as e:
    print(f"Ocurrió un error: {e}")
    
frutas = ["manzana", "banana", "naranja", "kiwi", "banana", "pera"]
mostrar_indice(frutas, "banana")
mostrar_indice(frutas, "sandia")

# count cuenta cuántas veces aparece un elemento en la lista
def contar_elemento(lista, elemento):
  try:
    print(f"El elemento {elemento} aparece {lista.count(elemento)} veces")
  except Exception as e:
    print(f"Ocurrió un error: {e}")
    
contar_elemento(frutas, "banana")
contar_elemento(frutas, "sandia")

# sort ordena la lista
def ordenar_lista(lista):
  lista.sort()
  print(f"La lista ordenada es {lista}")
  
ordenar_lista(frutas)

# reverse inverte el orden de la lista
def invertir_orden(lista):
  lista.reverse()
  print(f"La lista invertida es {lista}")
  
invertir_orden(frutas)

# clear borra la lista
def borrar_lista(lista):
  lista.clear()
  print(f"La lista borrada es {lista}")
  
borrar_lista(frutas)