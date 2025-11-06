import os

nombre = input("Ingrese su nombre: ")
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad = 2025 - año_nacimiento

# if os.system("clear") != 0: os.system("cls")
print(f"Hola {nombre}, tu edad es {edad}")
