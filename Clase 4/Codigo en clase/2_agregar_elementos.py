# append agrega elementos al final de la lista

def agregar_elemento(lista, elemento):
  lista.append(elemento)

lenguajes_programacion = ["Python", "Java", "C++", "JavaScript", "Ruby"]

agregar_elemento(lenguajes_programacion, "C#")

""" nuevo_lenguaje = input("Ingrese un nuevo lenguaje de programación: ")
agregar_elemento(lenguajes_programacion, nuevo_lenguaje) """

# insert inserta elementos en una posición determinada
def insertar_elemento(lista, elemento, indice):
  lista.insert(indice, elemento)
  
insertar_elemento(lenguajes_programacion, "Go", 2)
print(lenguajes_programacion)

# extend extiende la lista con otra lista
def extender_lista(lista1, lista2):
  lista1.extend(lista2)
  
l1 = [1, 2, 3]
l2 = [4, 5, 6]
extender_lista(l1, l2)
print(l1)
