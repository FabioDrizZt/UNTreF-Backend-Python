"""
Tests para Ejercicio 4: Tipo de Triángulo

Estos tests verifican que tu programa determine correctamente
el tipo de triángulo y valide si es un triángulo válido.
"""

import unittest
import os
import sys

def get_ejercicio_path():
    """Obtiene la ruta al archivo de ejercicio"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ejercicios_dir = os.path.join(script_dir, '..', 'ejercicios')
    return os.path.join(ejercicios_dir, 'TipoTriangulo.py')

from unittest.mock import patch
from io import StringIO

class TestTipoTriangulo(unittest.TestCase):
    """Tests para verificar el Ejercicio 4"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['5', '5', '5'])
    def test_triangulo_equilatero(self, mock_input, mock_stdout):
        """Prueba con lados 5, 5, 5 -> Equilátero"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Equilátero', output, "Con todos los lados iguales debe ser Equilátero")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['5', '5', '3'])
    def test_triangulo_isosceles(self, mock_input, mock_stdout):
        """Prueba con lados 5, 5, 3 -> Isósceles"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Isósceles', output, "Con dos lados iguales debe ser Isósceles")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['3', '4', '5'])
    def test_triangulo_escaleno(self, mock_input, mock_stdout):
        """Prueba con lados 3, 4, 5 -> Escaleno"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Escaleno', output, "Con todos los lados diferentes debe ser Escaleno")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', '2', '10'])
    def test_no_es_triangulo(self, mock_input, mock_stdout):
        """Prueba con lados 1, 2, 10 -> No es un triángulo"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('No es un triángulo', output, 
                         "Con lados que no cumplen la desigualdad triangular debe indicar que no es triángulo")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['6', '8', '10'])
    def test_triangulo_escaleno_pitagorico(self, mock_input, mock_stdout):
        """Prueba con lados 6, 8, 10 -> Escaleno"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Escaleno', output)
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['7', '10', '7'])
    def test_triangulo_isosceles_orden_diferente(self, mock_input, mock_stdout):
        """Prueba con lados 7, 10, 7 -> Isósceles"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Isósceles', output, "Debe detectar isósceles independiente del orden")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 4: Tipo de Triángulo")
    print("=" * 70)
    unittest.main(verbosity=2)

