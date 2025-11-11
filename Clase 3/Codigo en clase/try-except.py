""" 
en js seria try catch
try {
    // codigo que puede fallar
} catch (error) {
    // codigo que se ejecuta si el error ocurre
} finally {
    // codigo que se ejecuta tanto si el error ocurre como si no
}
"""
try:
  resultado = 1/0
  print(resultado)
except ZeroDivisionError:
  print("Error: Division por cero")
except TypeError:
  print("Error: Tipo de dato incorrecto")
except Exception as e:
  print(f"Error inesperado: {e}")
finally:
  print("Finalizado")
  
try:
  len(None)
  print("No se ejecuta")
except TypeError:
  print("Error: Tipo de dato incorrecto")
  
try:
  print(lalala)
except NameError:
  print("Error: No existe la variable")
  
frutas = ["manzana", "pera", "lima"]
""" print(frutas[10])
print("Esto no se ejecuta") """
try:
  print(frutas[10])
except IndexError:
  print("Error: Indice fuera de rango")
  
print("Esto si se ejecuta")

try:
  nro_tramite_dni = input("Ingrese el nro de tramite DNI: ")
  print(f"El nro de tramite es {nro_tramite_dni}")
except KeyboardInterrupt:
  print("\nEl usuario ha cancelado la operacion")

# Error al abrir archivo

try:
  with open("archivo.txt", "r") as archivo:
    print(archivo.read())
except FileNotFoundError:
  print("Error: Archivo no encontrado")
except Exception as e:
  print(f"Error: {e}")
  
# Excepciones personalizadas con raise

def saludar(nombre):
    if nombre == "D'artagnan":
        raise ValueError("En este app no se permiten nombres con 'D'artagnan")
    else:
        return f"Hola {nombre}"
      
try:
    print(saludar("D'artagnan"))
except ValueError as e:
    print(f"Error personalizado: {e}")
    
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
  
try:
    print(dividir(10, 0))
except ZeroDivisionError as e:
    print(f"Error personalizado: {e}")