"""
Tests para Ejercicio 8: Tienda de Descuento

Estos tests verifican que tu programa calcule correctamente
el monto final según el color de la bolita y el valor de la compra.
"""

import unittest
import os
import sys

def get_ejercicio_path():
    """Obtiene la ruta al archivo de ejercicio"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ejercicios_dir = os.path.join(script_dir, '..', 'ejercicios')
    return os.path.join(ejercicios_dir, 'TiendaDescuento.py')

from unittest.mock import patch
from io import StringIO

class TestTiendaDescuento(unittest.TestCase):
    """Tests para verificar el Ejercicio 8"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['100', 'blanca'])
    def test_bolita_blanca(self, mock_input, mock_stdout):
        """Prueba con compra 100 y bolita blanca -> 100 (0% descuento)"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('100', output, "Bolita blanca: sin descuento, debe ser 100")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['100', 'verde'])
    def test_bolita_verde(self, mock_input, mock_stdout):
        """Prueba con compra 100 y bolita verde -> 90 (10% descuento)"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('90', output, "Bolita verde: 10% descuento, debe ser 90")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['100', 'amarilla'])
    def test_bolita_amarilla(self, mock_input, mock_stdout):
        """Prueba con compra 100 y bolita amarilla -> 75 (25% descuento)"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('75', output, "Bolita amarilla: 25% descuento, debe ser 75")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['200', 'azul'])
    def test_bolita_azul(self, mock_input, mock_stdout):
        """Prueba con compra 200 y bolita azul -> 100 (50% descuento)"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('100', output, "Bolita azul: 50% descuento, debe ser 100")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['500', 'roja'])
    def test_bolita_roja(self, mock_input, mock_stdout):
        """Prueba con compra 500 y bolita roja -> 0 (100% descuento)"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('0', output, "Bolita roja: 100% descuento, debe ser 0")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['80', 'amarilla'])
    def test_bolita_amarilla_80(self, mock_input, mock_stdout):
        """Prueba con compra 80 y bolita amarilla -> 60 (25% descuento)"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('60', output, "Bolita amarilla: 25% descuento de 80 = 60")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 8: Tienda de Descuento")
    print("=" * 70)
    unittest.main(verbosity=2)

