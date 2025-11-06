"""
Tests para Ejercicio 9: Calificación de Estudiante

Estos tests verifican que tu programa asigne correctamente
la calificación según la nota del examen final.
"""

import unittest
import os
import sys

def get_ejercicio_path():
    """Obtiene la ruta al archivo de ejercicio"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ejercicios_dir = os.path.join(script_dir, '..', 'ejercicios')
    return os.path.join(ejercicios_dir, 'CalificacionEstudiante.py')

from unittest.mock import patch
from io import StringIO

class TestCalificacionEstudiante(unittest.TestCase):
    """Tests para verificar el Ejercicio 9"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='45')
    def test_calificacion_f(self, mock_input, mock_stdout):
        """Prueba con nota 45 -> F"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('F', output, "Con nota 45 la calificación debe ser F")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='65')
    def test_calificacion_d(self, mock_input, mock_stdout):
        """Prueba con nota 65 -> D"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('D', output, "Con nota 65 la calificación debe ser D")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='75')
    def test_calificacion_c(self, mock_input, mock_stdout):
        """Prueba con nota 75 -> C"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('C', output, "Con nota 75 la calificación debe ser C")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='85')
    def test_calificacion_b(self, mock_input, mock_stdout):
        """Prueba con nota 85 -> B"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('B', output, "Con nota 85 la calificación debe ser B")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='95')
    def test_calificacion_a(self, mock_input, mock_stdout):
        """Prueba con nota 95 -> A"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('A', output, "Con nota 95 la calificación debe ser A")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='0')
    def test_calificacion_limite_inferior_f(self, mock_input, mock_stdout):
        """Prueba con nota 0 -> F"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('F', output, "Con nota 0 la calificación debe ser F")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='100')
    def test_calificacion_limite_superior_a(self, mock_input, mock_stdout):
        """Prueba con nota 100 -> A"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('A', output, "Con nota 100 la calificación debe ser A")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='150')
    def test_nota_invalida_mayor(self, mock_input, mock_stdout):
        """Prueba con nota 150 -> Nota inválida"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('inválida', output.lower(), "Con nota > 100 debe mostrar nota inválida")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='-10')
    def test_nota_invalida_menor(self, mock_input, mock_stdout):
        """Prueba con nota -10 -> Nota inválida"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('inválida', output.lower(), "Con nota < 0 debe mostrar nota inválida")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 9: Calificación de Estudiante")
    print("=" * 70)
    unittest.main(verbosity=2)

