import pytest
import importlib

# El nombre del módulo comienza con un dígito, por lo que debemos usar importlib
# para importar el archivo como un módulo.
e_02_range = importlib.import_module("ejercicios.02_range")

def test_imprimir_1_al_10(capsys):
    """
    Test para Ejercicio 1: Imprimir números del 1 al 10.
    """
    e_02_range.imprimir_1_al_10()
    captured = capsys.readouterr()
    expected_output = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"
    assert captured.out == expected_output

def test_imprimir_impares_1_al_20(capsys):
    """
    Test para Ejercicio 2: Imprimir números impares del 1 al 20.
    """
    e_02_range.imprimir_impares_1_al_20()
    captured = capsys.readouterr()
    expected_output = "1\n3\n5\n7\n9\n11\n13\n15\n17\n19\n"
    assert captured.out == expected_output

def test_imprimir_multiplos_de_5(capsys):
    """
    Test para Ejercicio 3: Imprimir múltiplos de 5.
    """
    e_02_range.imprimir_multiplos_de_5()
    captured = capsys.readouterr()
    expected_output = "5\n10\n15\n20\n25\n30\n35\n40\n45\n50\n"
    assert captured.out == expected_output

def test_imprimir_inverso_10_al_1(capsys):
    """
    Test para Ejercicio 4: Imprimir números en orden inverso.
    """
    e_02_range.imprimir_inverso_10_al_1()
    captured = capsys.readouterr()
    expected_output = "10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n"
    assert captured.out == expected_output

def test_suma_1_al_100():
    """
    Test para Ejercicio 5: Suma de números en un rango.
    """
    # La suma de los primeros n números es n*(n+1)/2
    assert e_02_range.suma_1_al_100() == 5050

def test_tabla_multiplicar_range(capsys):
    """
    Test para Ejercicio 6: Tabla de multiplicar.
    """
    e_02_range.tabla_multiplicar_range(7)
    captured = capsys.readouterr()
    expected_lines = [f"7 x {i} = {7*i}" for i in range(1, 11)]
    expected_output = "\n".join(expected_lines) + "\n"
    assert captured.out == expected_output