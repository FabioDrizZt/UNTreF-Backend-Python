import os

i, fin, paso = 1, 11, 1
while i < fin:
    print(i)
    i += paso

i, fin, paso = 2, 11, 2
while i < fin:
    print(i)
    i += paso

i, fin, paso = 10, 0, -1
while i > fin:
    print(i)
    i += paso

frutas = ["manzana", "pera", "plátano", "limón"]
i = 0
while i < len(frutas):
    print(f"En la posicion {i+1} hay {frutas[i]}")
    i += 1

# Comportamiento de pila
while frutas:
    print(frutas.pop())

frutas = ["manzana", "pera", "plátano", "limón"]
# Comportamiento de cola
while frutas:
    print(frutas.pop(0))

os.system("cls")
# Emular do while
""" while True:
    print("Hola")
    if input("¿Quieres continuar? ") == "No":
        break """

# Juego de adivinacion del numero
# generamos un numero aleatorio
import random

numero_secreto = random.randint(1, 100)
nro_intentos = 0
while nro_intentos < 5:
    nro_intentos += 1
    numero_ingresado = int(input("Dime el numero: "))
    if numero_ingresado == numero_secreto:
        print("Felicidades! ¡Has ganado!")
        break
    if numero_ingresado < numero_secreto:
        print("el numero secreto es mayor")
        continue
    print("el numero secreto es menor")
else:
    print(f"Lo siento, no has ganado. El numero secreto es {numero_secreto}")
