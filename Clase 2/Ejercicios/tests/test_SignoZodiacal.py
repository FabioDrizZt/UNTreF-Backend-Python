"""
Tests para Ejercicio 6: Signo Zodiacal

Estos tests verifican que tu programa determine correctamente
el signo zodiacal según la fecha de nacimiento.
"""

import unittest
from unittest.mock import patch
from io import StringIO

class TestSignoZodiacal(unittest.TestCase):
    """Tests para verificar el Ejercicio 6"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['25', '3'])
    def test_signo_aries(self, mock_input, mock_stdout):
        """Prueba con 25 de marzo -> Aries"""
        try:
            with open('../ejercicios/SignoZodiacal.py', 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Aries', output, "El 25 de marzo es Aries")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['15', '5'])
    def test_signo_tauro(self, mock_input, mock_stdout):
        """Prueba con 15 de mayo -> Tauro"""
        try:
            with open('../ejercicios/SignoZodiacal.py', 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Tauro', output, "El 15 de mayo es Tauro")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['10', '6'])
    def test_signo_geminis(self, mock_input, mock_stdout):
        """Prueba con 10 de junio -> Géminis"""
        try:
            with open('../ejercicios/SignoZodiacal.py', 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Géminis', output, "El 10 de junio es Géminis")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['5', '8'])
    def test_signo_leo(self, mock_input, mock_stdout):
        """Prueba con 5 de agosto -> Leo"""
        try:
            with open('../ejercicios/SignoZodiacal.py', 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Leo', output, "El 5 de agosto es Leo")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['15', '12'])
    def test_signo_sagitario(self, mock_input, mock_stdout):
        """Prueba con 15 de diciembre -> Sagitario"""
        try:
            with open('../ejercicios/SignoZodiacal.py', 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Sagitario', output, "El 15 de diciembre es Sagitario")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', '1'])
    def test_signo_capricornio(self, mock_input, mock_stdout):
        """Prueba con 1 de enero -> Capricornio"""
        try:
            with open('../ejercicios/SignoZodiacal.py', 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Capricornio', output, "El 1 de enero es Capricornio")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['10', '2'])
    def test_signo_acuario(self, mock_input, mock_stdout):
        """Prueba con 10 de febrero -> Acuario"""
        try:
            with open('../ejercicios/SignoZodiacal.py', 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Acuario', output, "El 10 de febrero es Acuario")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 6: Signo Zodiacal")
    print("=" * 70)
    unittest.main(verbosity=2)

