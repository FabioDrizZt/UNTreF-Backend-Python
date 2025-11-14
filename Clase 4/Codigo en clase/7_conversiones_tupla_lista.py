print(type([1, 2, 3])) # list
print(type((1, 2, 3))) # tuple

paises_mercosur = ('AR', 'BR', 'PY', 'UY')
# paises_mercosur.append('BO')  # Error: las tuplas son inmutables
paises_mercosur = list(paises_mercosur)
paises_mercosur.append('BO')
paises_mercosur = tuple(paises_mercosur)
print(paises_mercosur)