nombre = "            D'artagnan\n es un  mosquetero           "
print(nombre)
nombre = nombre.strip()
print(nombre)

cadenasLargas = """
    Esta ES una barra  cadena larga
    """
    
# Metodos de cadenas
print(cadenasLargas.upper())
print(cadenasLargas.lower())

""" 
s.endswith(suffix)     # Verifica si termina con el sufijo
s.find(t)              # Primera aparición de t en s (o -1 si no está)
s.index(t)             # Primera aparición de t en s (error si no está)
s.isalpha()            # Verifica si los caracteres son alfabéticos
s.isdigit()            # Verifica si los caracteres son numéricos
s.islower()            # Verifica si los caracteres son minúsculas
s.isupper()            # Verifica si los caracteres son mayúsculas
s.join(slist)          # Une una lista de cadenas usando s como delimitador
s.lower()              # Convertir a minúsculas
s.replace(old,new)     # Reemplaza texto
s.split([delim])       # Parte la cadena en subcadenas
s.startswith(prefix)   # Verifica si comienza con un prefijo
s.strip()              # Elimina espacios en blanco al inicio o al final
s.upper()              # Convierte a mayúsculas
"""

# Indexación de cadenas
a = "Hola mundo"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])

print(a[:5])
print(a[5:])
print(a[-2:])
print(a[5:8])

