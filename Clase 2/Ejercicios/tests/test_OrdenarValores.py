"""
Tests para Ejercicio 3: Ordenar Valores

Estos tests verifican que tu programa ordene correctamente
tres valores de menor a mayor.
"""

import unittest
from unittest.mock import patch
from io import StringIO

class TestOrdenarValores(unittest.TestCase):
    """Tests para verificar el Ejercicio 3"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['3', '1', '2'])
    def test_ordenar_desordenados(self, mock_input, mock_stdout):
        """Prueba con 3, 1, 2 -> 1, 2, 3"""
        try:
            with open('../ejercicios/OrdenarValores.py', 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('1', output, "Debe aparecer el 1")
            self.assertIn('2', output, "Debe aparecer el 2")
            self.assertIn('3', output, "Debe aparecer el 3")
            
            # Verificar el orden
            pos1 = output.find('1')
            pos2 = output.find('2')
            pos3 = output.find('3')
            
            self.assertLess(pos1, pos2, "El 1 debe aparecer antes que el 2")
            self.assertLess(pos2, pos3, "El 2 debe aparecer antes que el 3")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['10', '5', '15'])
    def test_ordenar_medio_menor(self, mock_input, mock_stdout):
        """Prueba con 10, 5, 15 -> 5, 10, 15"""
        try:
            with open('../ejercicios/OrdenarValores.py', 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            pos5 = output.find('5')
            pos10 = output.find('10')
            pos15 = output.find('15')
            
            self.assertLess(pos5, pos10, "El 5 debe aparecer antes que el 10")
            self.assertLess(pos10, pos15, "El 10 debe aparecer antes que el 15")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['100', '200', '50'])
    def test_ordenar_ultimo_menor(self, mock_input, mock_stdout):
        """Prueba con 100, 200, 50 -> 50, 100, 200"""
        try:
            with open('../ejercicios/OrdenarValores.py', 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            pos50 = output.find('50')
            pos100 = output.find('100')
            pos200 = output.find('200')
            
            self.assertLess(pos50, pos100, "El 50 debe aparecer antes que el 100")
            self.assertLess(pos100, pos200, "El 100 debe aparecer antes que el 200")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['-5', '0', '10'])
    def test_ordenar_con_negativos(self, mock_input, mock_stdout):
        """Prueba con -5, 0, 10 -> -5, 0, 10"""
        try:
            with open('../ejercicios/OrdenarValores.py', 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('-5', output)
            self.assertIn('0', output)
            self.assertIn('10', output)
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 3: Ordenar Valores")
    print("=" * 70)
    unittest.main(verbosity=2)

