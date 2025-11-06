edad = 18 # int(input("Ingrese su edad: "))

""" en js
    if (edad >= 18) {
        console.log("Eres mayor de edad")
    }
"""

if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes conducir")
    
nombre = "Fabio" # input("Ingrese su nombre: ")
if nombre == 'Fabio':
    print("Eres un genio")

print("Fin del programa.")

# Que numero es el mayor ?
a,b,c = 5,6,7

if a>b>c or a>c>b:
    print("El mayor es a")
elif b>c:
    print("El mayor es b")
else:
    print("El mayor es c")