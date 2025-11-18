import pytest
import importlib

# El nombre del módulo comienza con un dígito, por lo que debemos usar importlib
# para importar el archivo como un módulo.
e_01_list = importlib.import_module("ejercicios.01_list")

def test_extraer_mensaje_secreto():
    """
    Test para Ejercicio 1: El mensaje secreto.
    """
    mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
    assert e_01_list.extraer_mensaje_secreto(mensaje) == ["s", "e", "c", "r", "e", "t", "o"]

def test_intercambiar_primero_y_ultimo():
    """
    Test para Ejercicio 2: Intercambio de posiciones.
    """
    numeros = [10, 20, 30, 40, 50]
    e_01_list.intercambiar_primero_y_ultimo(numeros)
    assert numeros == [50, 20, 30, 40, 10]
    
    lista_corta = [1, 2]
    e_01_list.intercambiar_primero_y_ultimo(lista_corta)
    assert lista_corta == [2, 1]

def test_crear_sandwich():
    """
    Test para Ejercicio 3: El sándwich de listas.
    """
    pan = ["pan arriba"]
    ingredientes = ["jamón", "queso", "tomate"]
    pan_abajo = ["pan abajo"]
    assert e_01_list.crear_sandwich(pan, ingredientes, pan_abajo) == ["pan arriba", "jamón", "queso", "tomate", "pan abajo"]

def test_duplicar_lista():
    """
    Test para Ejercicio 4: Duplicando la lista.
    """
    assert e_01_list.duplicar_lista([1, 2, 3]) == [1, 2, 3, 1, 2, 3]
    assert e_01_list.duplicar_lista(["a", "b"]) == ["a", "b", "a", "b"]
    assert e_01_list.duplicar_lista([]) == []

def test_extraer_elemento_central():
    """
    Test para Ejercicio 5: Extrayendo el centro.
    """
    assert e_01_list.extraer_elemento_central([10, 20, 30, 40, 50]) == 30
    assert e_01_list.extraer_elemento_central(["a", "b", "c"]) == "b"
    assert e_01_list.extraer_elemento_central([1]) == 1

def test_invertir_primera_mitad():
    """
    Test para Ejercicio 6: Reversa parcial.
    """
    assert e_01_list.invertir_primera_mitad([1, 2, 3, 4, 5, 6]) == [3, 2, 1, 4, 5, 6]
    assert e_01_list.invertir_primera_mitad([10, 20, 30, 40]) == [20, 10, 30, 40]
    assert e_01_list.invertir_primera_mitad([1, 2, 3]) == [1, 2, 3] # La mitad de 3 es 1, no se invierte.
    assert e_01_list.invertir_primera_mitad([]) == []