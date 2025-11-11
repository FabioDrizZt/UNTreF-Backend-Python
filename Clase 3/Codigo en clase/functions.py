# def nombre_funcion(parametros):
#     # codigo
#     return valor

def saludo():
  return "Hola mundo"
  
print(saludo())

def saludo(nombre):
  return f"Hola {nombre}"
  
print(saludo("D'artagnan"))

def saludo(nombre, edad):
  return f"Hola {nombre} tu edad es {edad}"
  
print(saludo("D'artagnan", 21))

# parametros por defecto
def saludo(nombre, edad=25):
  return f"Hola {nombre} tu edad es {edad}"

print(saludo("D'artagnan"))

# argumentos por posicion
def saludo(nombre: str, edad: int):
  return f"Hola {nombre} tu edad es {edad}"

print(saludo(edad=21, nombre='D\'artagnan'))

# operador splat *
def saludo(*nombres):
  return f"Hola {nombres}"

print(saludo("D'artagnan", "Fabio", "Juan"))

""" 
function sumar(...args) {
    let total = 0;
    for (let arg of args) {
        total += arg;
    }
    return total;
}
"""

def sumar(*args):
    total = 0
    for arg in args:
        total += arg
    return total
    
print(sumar(1, 2, 3))
print(sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def mostrarInformacion(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")
    
mostrarInformacion(nombre="D'artagnan", edad=25, profesion="Musketero", pais="Francia")
 

""" en js son arrow functions
const saludar = nombre => `Hola ${nombre}`;
const sumar = (a, b) => a + b;
"""

# lambda functions: solamente para funciones de una sola linea
saludar = lambda nombre: f"Hola {nombre}"
sumar = lambda a, b: a + b

def doble(n): return n * 2
doble = lambda n: n * 2

print(doble(2))