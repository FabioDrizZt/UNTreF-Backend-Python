# remove quita el primer elemento que coincide con el valor pasado

def quitar_elemento_valor(lista, elemento):
  try:
    lista.remove(elemento)
    print(f"Se ha quitado el elemento {elemento}")
  except ValueError:
    print(f"No se puede quitar el elemento {elemento}")
  """ else: # solo se ejecuta si no hubo error
    print(f"Se ha quitado el elemento {elemento}") """
    
frutas = ["manzana", "banana", "naranja", "kiwi", "banana", "pera"]

quitar_elemento_valor(frutas, "banana")
quitar_elemento_valor(frutas, "banana")
quitar_elemento_valor(frutas, "banana")


""" # len de dict
print(len({"clave": "valor", "clave2": "valor2", "clave3": "valor3"}))
 """
# pop elimina elemento de una posicion dada y lo retorna
def quitar_elemento_posicion(lista, posicion):
  try:
    lista.pop(posicion)
    print(f"Se ha quitado el elemento en la posicion {posicion}")
  except IndexError:
    print(f"No se puede quitar el element en la posicion {posicion}")
  except Exception as e:
    print(f"Ocurrió un error: {e}")
    
quitar_elemento_posicion(frutas, 1)
quitar_elemento_posicion(frutas, 5)
print(frutas)