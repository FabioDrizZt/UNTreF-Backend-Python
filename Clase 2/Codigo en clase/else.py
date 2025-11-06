edad = 17

if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes conducir")
elif edad >= 16:
    print("Eres CASE mayor de edad")
    print("Puedes conducir con permiso de papa y mama")
else:
    print("No eres mayor de edad")
    print("No puedes conducir")
     

print("MENU DE OPCIONES")
print("1. Ingresar datos")
print("2. Ordenar datos")
print("3. Eliminar datos")
print("4. Salir")
opcion = int(input("Elija una opcion: "))

if (opcion < 1 or opcion > 4):
    print("Opcion invalida")
elif opcion == 1:
    print("Ingresando datos")
elif opcion == 2:
    print("Ordenando datos")
elif opcion == 3:
    print("Eliminando datos")
else:
    print("Saliendo del programa")
    
print("Fin del programa.")
