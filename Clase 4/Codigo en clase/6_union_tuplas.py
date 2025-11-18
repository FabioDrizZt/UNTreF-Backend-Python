paises_mercosur = ('AR', 'BR', 'PY', 'UY')
paises_andinos = ('BO', 'CO', 'EC', 'PE', 'VE')

paises_region = paises_mercosur + paises_andinos
print(paises_region)

paises_region_extendido = paises_region + ('CL', 'SR', 'GY', 'GF')
print(paises_region_extendido)

# zip
nombres = ['Juan', 'Pedro', 'Carlos', 'Luis']
edades = [25, 30, 18, 20]
ciudades = ['Buenos Aires', 'Rosario', 'Santiago', 'Mendoza']

datos_personas = zip(nombres, edades, ciudades)

for nombre, edad, ciudad in datos_personas:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")