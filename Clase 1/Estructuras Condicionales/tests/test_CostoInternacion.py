"""
Tests para Ejercicio 7: Costo de Internación

Estos tests verifican que tu programa calcule correctamente
el costo total de internación según el tipo de enfermedad,
edad del paciente y días de internación.
"""

import unittest
import os
import sys

def get_ejercicio_path():
    """Obtiene la ruta al archivo de ejercicio"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ejercicios_dir = os.path.join(script_dir, '..', 'ejercicios')
    return os.path.join(ejercicios_dir, 'CostoInternacion.py')

from unittest.mock import patch
from io import StringIO

class TestCostoInternacion(unittest.TestCase):
    """Tests para verificar el Ejercicio 7"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', '10', '2'])
    def test_tipo1_menor_14(self, mock_input, mock_stdout):
        """Prueba tipo 1, 10 años, 2 días -> 425 * 2 = 850 (sin recargo)"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('850', output, "Tipo 1, edad < 14, sin recargo: 425 * 2 = 850")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', '18', '1'])
    def test_tipo1_entre_14_22(self, mock_input, mock_stdout):
        """Prueba tipo 1, 18 años, 1 día -> 425 * 1.10 * 1 = 467.5"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Puede aparecer como 467.5 o 467,5
            tiene_costo = '467.5' in output or '467,5' in output or '467.50' in output
            self.assertTrue(tiene_costo, "Tipo 1, edad 18, recargo 10%: 425 * 1.10 = 467.5")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', '30', '1'])
    def test_tipo1_mayor_22(self, mock_input, mock_stdout):
        """Prueba tipo 1, 30 años, 1 día -> 425 * 1.20 * 1 = 510"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('510', output, "Tipo 1, edad > 22, recargo 20%: 425 * 1.20 = 510")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['2', '10', '1'])
    def test_tipo2_menor_14(self, mock_input, mock_stdout):
        """Prueba tipo 2, 10 años, 1 día -> 800 (sin recargo)"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('800', output, "Tipo 2, edad < 14, sin recargo: 800")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['3', '25', '1'])
    def test_tipo3_mayor_22(self, mock_input, mock_stdout):
        """Prueba tipo 3, 25 años, 1 día -> 1500 * 1.20 = 1800"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('1800', output, "Tipo 3, edad > 22, recargo 20%: 1500 * 1.20 = 1800")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['2', '20', '3'])
    def test_tipo2_edad_20_varios_dias(self, mock_input, mock_stdout):
        """Prueba tipo 2, 20 años, 3 días -> 800 * 1.10 * 3 = 2640"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('2640', output, "Tipo 2, edad 20, 3 días, recargo 10%: 800 * 1.10 * 3 = 2640")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 7: Costo de Internación")
    print("=" * 70)
    unittest.main(verbosity=2)

