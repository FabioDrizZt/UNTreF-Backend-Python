"""
Tests para Ejercicio 2: Institución de Educación

Estos tests verifican que tu programa determine correctamente el estado
del estudiante según su nota y carrera (diurna o vespertina).
"""

import unittest
import os
import sys

def get_ejercicio_path():
    """Obtiene la ruta al archivo de ejercicio"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ejercicios_dir = os.path.join(script_dir, '..', 'ejercicios')
    return os.path.join(ejercicios_dir, 'InstitucionEducacion.py')

from unittest.mock import patch
from io import StringIO

class TestInstitucionEducacion(unittest.TestCase):
    """Tests para verificar el Ejercicio 2"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['4.5', 'diurna'])
    def test_diurna_aprobado(self, mock_input, mock_stdout):
        """Prueba diurna con nota 4.5 -> Aprobado"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Aprobado', output, "Con nota 4.5 en diurna debe estar Aprobado")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['3.0', 'diurna'])
    def test_diurna_reprobado(self, mock_input, mock_stdout):
        """Prueba diurna con nota 3.0 -> Reprobado"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Reprobado', output, "Con nota 3.0 en diurna debe estar Reprobado")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['4.5', 'vespertina'])
    def test_vespertina_aprobado(self, mock_input, mock_stdout):
        """Prueba vespertina con nota 4.5 -> Aprobado"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Aprobado', output, "Con nota 4.5 en vespertina debe estar Aprobado")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['3.7', 'vespertina'])
    def test_vespertina_recuperacion(self, mock_input, mock_stdout):
        """Prueba vespertina con nota 3.7 -> Recuperación"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Recuperación', output, 
                         "Con nota 3.7 en vespertina debe estar en Recuperación")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['3.0', 'vespertina'])
    def test_vespertina_reprobado(self, mock_input, mock_stdout):
        """Prueba vespertina con nota 3.0 -> Reprobado"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Reprobado', output, "Con nota 3.0 en vespertina debe estar Reprobado")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['4.0', 'diurna'])
    def test_diurna_limite_aprobado(self, mock_input, mock_stdout):
        """Prueba diurna con nota 4.0 exacta -> Aprobado"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Aprobado', output, "Con nota 4.0 en diurna debe estar Aprobado")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 2: Institución de Educación")
    print("=" * 70)
    unittest.main(verbosity=2)

