"""
Tests para Ejercicio 5: Fecha con Nombre del Mes

Estos tests verifican que tu programa muestre correctamente
la fecha con el nombre del mes en lugar del número.
"""

import unittest
from unittest.mock import patch
from io import StringIO

class TestFechaNombreMes(unittest.TestCase):
    """Tests para verificar el Ejercicio 5"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['15', '3', '2023'])
    def test_fecha_marzo(self, mock_input, mock_stdout):
        """Prueba con 15/3/2023 -> 15 de marzo de 2023"""
        try:
            with open('../ejercicios/FechaNombreMes.py', 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('15', output, "Debe incluir el día")
            self.assertIn('marzo', output.lower(), "Debe mostrar 'marzo'")
            self.assertIn('2023', output, "Debe incluir el año")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', '1', '2024'])
    def test_fecha_enero(self, mock_input, mock_stdout):
        """Prueba con 1/1/2024 -> 1 de enero de 2024"""
        try:
            with open('../ejercicios/FechaNombreMes.py', 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('1', output)
            self.assertIn('enero', output.lower())
            self.assertIn('2024', output)
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['25', '12', '2025'])
    def test_fecha_diciembre(self, mock_input, mock_stdout):
        """Prueba con 25/12/2025 -> 25 de diciembre de 2025"""
        try:
            with open('../ejercicios/FechaNombreMes.py', 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('25', output)
            self.assertIn('diciembre', output.lower())
            self.assertIn('2025', output)
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['10', '7', '2020'])
    def test_fecha_julio(self, mock_input, mock_stdout):
        """Prueba con 10/7/2020 -> 10 de julio de 2020"""
        try:
            with open('../ejercicios/FechaNombreMes.py', 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('10', output)
            self.assertIn('julio', output.lower())
            self.assertIn('2020', output)
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['20', '6', '2022'])
    def test_fecha_junio(self, mock_input, mock_stdout):
        """Prueba con 20/6/2022 -> 20 de junio de 2022"""
        try:
            with open('../ejercicios/FechaNombreMes.py', 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('20', output)
            self.assertIn('junio', output.lower())
            self.assertIn('2022', output)
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 5: Fecha con Nombre del Mes")
    print("=" * 70)
    unittest.main(verbosity=2)

