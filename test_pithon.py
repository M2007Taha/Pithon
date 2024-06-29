import pytest
from pithon import main

class GUI:
    def __init__(self):
        self.outputs = {
            "factorial_out": [],
            "fibonacci_out": [],
            "trigonometry_out": [],
            "exponentiation_out": [],
            "absolute_out": [],
            "gcd_lcm_out": []
        }
        self.inputs = {
            "factorial_input": "5",
            "fibonacci_input": "5",
            "trigonometry_input": "45",
            "exponentiation_exponent_input": "2",
            "exponentiation_base_input": "3",
            "absolute_input": "-5",
            "gcd_lcm_input1": "5",
            "gcd_lcm_input2": "10"
        }

@pytest.fixture
def app():
    gui = GUI()
    return main(gui)

def test_fibonacci_func(app):
    app.fibonacci_func()
    assert app.gui.outputs["fibonacci_out"] == [], "Fibonacci output is incorrect"

def test_factorial_func(app):
    app.factorial_func()
    assert app.gui.outputs["factorial_out"] == [], "Factorial output is incorrect"
    
def test_trigonometry_func(app):
    app.trigonometry_func()
    assert app.gui.outputs["trigonometry_out"] == []

def test_exponentiation_func(app):
    app.exponentiation_func()
    assert app.gui.outputs["exponentiation_out"] == []
def test_absolute_func(app):
    app.absolute_func()
    assert app.gui.outputs["absolute_out"] == []
def test_gcd_lcm_func(app):
    app.gcd_lcm_func()
    assert app.gui.outputs['gcd_lcm_out'] == []
def test_clear(app):
    assert app.gui.outputs == {
            "factorial_out": [],
            "fibonacci_out": [],
            "trigonometry_out": [],
            "exponentiation_out": [],
            "absolute_out": [],
            "gcd_lcm_out": []
        }
    
if __name__ == "__main__":
    pytest.main(['-v', 'test_pithon.py'])
