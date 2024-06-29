"""
@author: m2007taha
digital_transformation_in_mathematics v1.0
"""
from sys import exit , argv
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from math import radians, sin, cos, tan, gcd, lcm

class main():
    def __init__(self,gui):
        self.gui = gui
    def func(self):
        self.gui.factorial_button.clicked.connect(self.clear)
        self.gui.factorial_button.clicked.connect(self.factorial_func)
        self.gui.trigonometry_button.clicked.connect(self.clear)
        self.gui.trigonometry_button.clicked.connect(self.trigonometry_func)
        self.gui.fibonacci_button.clicked.connect(self.clear)
        self.gui.fibonacci_button.clicked.connect(self.fibonacci_func)
        self.gui.exponentiation_button.clicked.connect(self.clear)
        self.gui.exponentiation_button.clicked.connect(self.exponentiation_func)
        self.gui.absolute_button.clicked.connect(self.clear)
        self.gui.absolute_button.clicked.connect(self.absolute_func)
        self.gui.gcd_lcm_button.clicked.connect(self.clear)
        self.gui.gcd_lcm_button.clicked.connect(self.gcd_lcm_func)
    #functions
    def fibonacci_func(self):
        try:
            print("fibonacci function run")
            counter = int(self.gui.fibonacci_input.text())
            a, b = 1, 1
            for _ in range(0,counter):
                self.gui.fibonacci_out.append(f"{a}\n")
                print(a, end=" ")
                a, b = b, a+b
            print()
        except:
            print('Error')
    def factorial_func(self):
        try:
            print("factorial function run")
            pin = self.gui.factorial_input.text()
            if '-' in pin:
                number = int(pin.replace('-',''))
                tmp = '-'
            else:
                number = int(pin)
                tmp = ''
            print(f"user input : {number}")
            factor = number * (number-1)
            for i in range(number-2,0,-1):
                factor *= i
            self.gui.factorial_out.append(f'{tmp}{factor}')
            print(f'out put : {tmp}{factor}')
        except:
            print('Error')
    def trigonometry_func(self):
        try:
            print("trigonometry function run")
            Input = self.gui.trigonometry_input.text()
            angle = radians(int(Input))
            print(f"user input : {angle}")
            _sin = round(sin(angle),5)
            _cos = round(cos(angle),5)
            _tan = round(tan(angle),5)
            if tan != 0 :
                _cot = round((1 / _tan),5)
            else: 
                _cot = 'Undefinde - تعریف نشده'
            result = f"sin{Input}∘ : {_sin}\ncos{Input}∘ : {_cos}\ntan{Input}∘ : {_tan}\ncot{Input}∘ : {_cot}"
            self.gui.trigonometry_out.append(f'{result}')
            print(f'out put :\n{result}')
        except:
            print('Error')
    def exponentiation_func(self):
        try:
            print("exponentiation function run")
            exponent = float(self.gui.exponentiation_exponent_input.text())
            base = float(self.gui.exponentiation_base_input.text())
            print(f"user input:\nexponent : {exponent}\nbase : {base}")
            result = round(pow(base,exponent),2)
            self.gui.exponentiation_out.append(f"{result}")
            print(f"out put : {result}")
        except ZeroDivisionError:
            self.gui.exponentiation_out.append(f"{'Undefinde - تعریف نشده'}")
            print(f"out put : {'Undefinde - تعریف نشده'}")
        except:
            print('Error')
    def absolute_func(self):
        try:
            print("absolute function run")
            number = float(self.gui.absolute_input.text())
            print(f"user input : {number}")
            if number in {0,1}:
                result = 1
            else:
                result = abs(number)
            self.gui.absolute_out.append(f'{result}')
            print(f"out put : {result}")
        except:
            print('Error')
    def gcd_lcm_func(self):
        try:
            print("gcd_lcm function run")
            number1 = int(self.gui.gcd_lcm_input1.text())
            number2 = int(self.gui.gcd_lcm_input2.text())
            print(f"user input : {number1},{number2}")
            _gcd = gcd(number1,number2)
            _lcm = lcm(number1,number2)
            result = f"GCD({number1},{number2}) = {_gcd}\nLCM({number1},{number2}) = {_lcm}"
            self.gui.gcd_lcm_out.append(result)
            print(f"out put : {result}")
        except:
            print('Error')
    def clear(self):
        print('clear function run')
        self.gui.trigonometry_out.clear()
        self.gui.factorial_out.clear()
        self.gui.fibonacci_out.clear()
        self.gui.exponentiation_out.clear()
        self.gui.absolute_out.clear()
        self.gui.gcd_lcm_out.clear()

if __name__ == "__main__":
    app = QApplication(argv)
    ui_file = QFile('pithon.ui')
    if not ui_file.open(QIODevice.ReadOnly):
        exit('error: cannot open *.ui file')
    loader=QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        exit(loader.errorString())
    window.setWindowTitle('πthon')
    window.setWindowIcon(QIcon('icone.png'))
    window.setCentralWidget(window.main_tabs)
    window.show()
    a = main(window)
    a.func()
    exit(app.exec())
