import pytest
import importlib
import io
import sys

# El nombre del módulo comienza con un dígito, por lo que debemos usar importlib
# para importar el archivo como un módulo.
e_04_while = importlib.import_module("ejercicios.04_while")

def test_cuenta_atras(capsys):
    """
    Test para el Ejercicio 1: Cuenta atrás.
    Verifica que la función imprime los números del 10 al 1.
    """
    e_04_while.cuenta_atras()
    captured = capsys.readouterr()
    expected_output = "10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n"
    assert captured.out == expected_output

def test_suma_pares():
    """
    Test para el Ejercicio 2: Suma de números pares.
    Verifica que la función devuelve la suma correcta de los números pares del 1 al 20.
    """
    assert e_04_while.suma_pares() == 110

def test_factorial():
    """
    Test para el Ejercicio 3: Factorial de un número.
    Verifica que la función calcula el factorial correctamente para varios casos.
    """
    assert e_04_while.factorial(5) == 120
    assert e_04_while.factorial(0) == 1
    assert e_04_while.factorial(1) == 1
    with pytest.raises(ValueError):
        e_04_while.factorial(-5)

def test_validar_contrasena():
    """
    Test para el Ejercicio 4: Validación de contraseña.
    Verifica que la función valida correctamente la longitud de la contraseña.
    """
    assert e_04_while.validar_contrasena("passwordvalido") is True
    assert e_04_while.validar_contrasena("12345678") is True
    assert e_04_while.validar_contrasena("corta") is False
    assert e_04_while.validar_contrasena("") is False

def test_tabla_multiplicar(capsys):
    """
    Test para el Ejercicio 5: Tabla de multiplicar.
    Verifica que la función imprime la tabla de multiplicar de un número.
    """
    e_04_while.tabla_multiplicar(3)
    captured = capsys.readouterr()
    expected_lines = [f"3 x {i} = {3*i}" for i in range(1, 11)]
    expected_output = "\n".join(expected_lines) + "\n"
    assert captured.out == expected_output

def test_numeros_primos_hasta_n(capsys):
    """
    Test para el Ejercicio 6: Números primos hasta N.
    Verifica que la función imprime los números primos hasta un número N.
    """
    e_04_while.numeros_primos_hasta_n(10)
    captured = capsys.readouterr()
    assert captured.out == "2\n3\n5\n7\n"

    e_04_while.numeros_primos_hasta_n(2)
    captured = capsys.readouterr()
    assert captured.out == "2\n"

    e_04_while.numeros_primos_hasta_n(1)
    captured = capsys.readouterr()
    assert captured.out == ""
