import os

# Recorrer una lista
frutas = ["manzana", "pera", "plátano", "limón"]

for fruta in frutas:
    print(fruta)

tupla_lenguajes = ("Python", "Java", "C++", "JavaScript")

for lenguaje in tupla_lenguajes:
    print(lenguaje)

# Mostrar datos de varias listas
productos = ["Laptop", "Mouse", "Teclado"]
precios = [1000, 25, 75]
stock = [10, 20, 30]

for producto, precio, stock in zip(productos, precios, stock):
    print(f"{producto}: ${precio}, Stock: {stock}")

# operacion sobre rangos
for i in range(len(frutas)):
    print(i)

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(2, 11, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)


# mostrar indice y valor en una lista
for i, valor in enumerate(frutas, start=1):
    print(f"En la posicion {i} hay {valor}")

# Interrupciones de bucles: break y continue

numeros = [3, 7, 8, 12, -5, -6, 15, 16, 17]

for n in numeros:
    if n == 0:
        print(f"Se encontro un 0 y se cortó el bucle")
        break
    if n < 0:
        print(f"Encontrado {n} es negativo no se evalua la paridad")
        continue
    if n % 2 == 0:
        print(f"Encontrado {n} es par")
        continue
    print(f"Encontrado {n} es impar")
else: # Permite saber si se ejecutaron todas las iteraciones del bucle
    print("No hubo un error en la entrada de datos")

# Sin continue
for n in numeros:
    if n == 0:
        print(f"Se encontro un 0 y se cortó el bucle")
        break
    if n < 0:
        print(f"Encontrado {n} es negativo no se evalua la paridad")        
    elif n % 2 == 0:
        print(f"Encontrado {n} es par")
    else:
        print(f"Encontrado {n} es impar")
else: 
    print("No hubo un error en la entrada de datos")

# List comprehension
cuadrados = [i**2 for i in numeros]
print(cuadrados)

edades = [25, 30, 18, 20, 28, 12, 15, 35, 40]
mayores = [edad for edad in edades if edad >= 18]
print(mayores)

numeros = [3, 7, 8, 12, -5, -6, 15, 16, 17]
etiquetas = ["negativo" if n < 0 else "positivo" for n in numeros]
print(etiquetas)

os.system("cls")

""" 
pass es el equivalente en js o c++: {}

en js:
for(let i = 0; i < 10; i++) {
    if (n%2 == 0) {
        // TODO: Enviar este dato a la BD
    }
    print(f"El numero leido es {n}")
}
"""
def funcionARealizar(n):
    # TODO: realizar esta funcion mas adelante
    pass # si no se pone pass no se ejecuta el codigo
funcionARealizar(3)

numeros = [3, 7, 8, 12, -5, -6, 15, 16, 17]
for n in numeros:
    if n % 2 == 0:
        # TODO: Enviar este dato a la BD
        pass
        print(f"{n} es par")
    print(f"El numero leido es {n}")
        