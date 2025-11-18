import pytest
import importlib

# El nombre del módulo comienza con un dígito, por lo que debemos usar importlib
# para importar el archivo como un módulo.
e_03_for = importlib.import_module("ejercicios.03_for")

def test_imprimir_pares_for(capsys):
    """
    Test para Ejercicio 1: Imprimir números pares.
    """
    e_03_for.imprimir_pares_for()
    captured = capsys.readouterr()
    expected_output = "2\n4\n6\n8\n10\n12\n14\n16\n18\n20\n"
    assert captured.out == expected_output

def test_calcular_media():
    """
    Test para Ejercicio 2: Calcular la media de una lista.
    """
    assert e_03_for.calcular_media([10, 20, 30, 40, 50]) == 30.0
    assert e_03_for.calcular_media([1, 2, 3, 4, 5]) == 3.0
    assert e_03_for.calcular_media([]) == 0.0

def test_buscar_maximo():
    """
    Test para Ejercicio 3: Buscar el máximo de una lista.
    """
    assert e_03_for.buscar_maximo([15, 5, 25, 10, 20]) == 25
    assert e_03_for.buscar_maximo([-1, -5, -2]) == -1
    with pytest.raises(ValueError):
        e_03_for.buscar_maximo([])

def test_filtrar_palabras_por_longitud():
    """
    Test para Ejercicio 4: Filtrar cadenas por longitud.
    """
    palabras = ["casa", "arbol", "sol", "elefante", "luna"]
    assert e_03_for.filtrar_palabras_por_longitud(palabras, 5) == ["elefante"]
    assert e_03_for.filtrar_palabras_por_longitud(palabras, 3) == ["casa", "arbol", "elefante", "luna"]
    assert e_03_for.filtrar_palabras_por_longitud(palabras, 10) == []

def test_contar_palabras_por_letra():
    """
    Test para Ejercicio 5: Contar palabras que empiezan con una letra.
    """
    palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
    assert e_03_for.contar_palabras_por_letra(palabras, "c") == 2
    assert e_03_for.contar_palabras_por_letra(palabras, "C") == 2
    assert e_03_for.contar_palabras_por_letra(palabras, "a") == 1
    assert e_03_for.contar_palabras_por_letra(palabras, "z") == 0
