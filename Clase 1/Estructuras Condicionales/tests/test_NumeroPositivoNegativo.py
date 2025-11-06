"""
Tests para Ejercicio 1: Número Positivo o Negativo

Estos tests verifican que tu programa determine correctamente
el signo (positivo/negativo/cero) y la paridad (par/impar) de un número.
"""

import unittest
import os
import sys

def get_ejercicio_path():
    """Obtiene la ruta al archivo de ejercicio"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ejercicios_dir = os.path.join(script_dir, '..', 'ejercicios')
    return os.path.join(ejercicios_dir, 'NumeroPositivoNegativo.py')

from unittest.mock import patch
from io import StringIO

class TestNumeroPositivoNegativo(unittest.TestCase):
    """Tests para verificar el Ejercicio 1"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='4')
    def test_numero_positivo_par(self, mock_input, mock_stdout):
        """Prueba con 4 -> positivo, par"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue().lower()
            
            self.assertIn('positivo', output, "Debe identificar que 4 es positivo")
            self.assertIn('par', output, "Debe identificar que 4 es par")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='-5')
    def test_numero_negativo_impar(self, mock_input, mock_stdout):
        """Prueba con -5 -> negativo, impar"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue().lower()
            
            self.assertIn('negativo', output, "Debe identificar que -5 es negativo")
            self.assertIn('impar', output, "Debe identificar que -5 es impar")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='0')
    def test_numero_cero(self, mock_input, mock_stdout):
        """Prueba con 0 -> cero, par"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue().lower()
            
            self.assertIn('cero', output, "Debe identificar que 0 es cero")
            self.assertIn('par', output, "Debe identificar que 0 es par")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='7')
    def test_numero_positivo_impar(self, mock_input, mock_stdout):
        """Prueba con 7 -> positivo, impar"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue().lower()
            
            self.assertIn('positivo', output)
            self.assertIn('impar', output)
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='-8')
    def test_numero_negativo_par(self, mock_input, mock_stdout):
        """Prueba con -8 -> negativo, par"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue().lower()
            
            self.assertIn('negativo', output)
            self.assertIn('par', output)
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 1: Número Positivo o Negativo")
    print("=" * 70)
    unittest.main(verbosity=2)

