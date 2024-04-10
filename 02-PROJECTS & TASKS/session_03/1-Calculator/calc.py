import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # Create the input field
        self.input_field = QLineEdit(self)

        # Create the buttons
        self.btn_1 = QPushButton('1', self)
        self.btn_2 = QPushButton('2', self)
        self.btn_3 = QPushButton('3', self)
        self.btn_4 = QPushButton('4', self)
        self.btn_5 = QPushButton('5', self)
        self.btn_6 = QPushButton('6', self)
        self.btn_7 = QPushButton('7', self)
        self.btn_8 = QPushButton('8', self)
        self.btn_9 = QPushButton('9', self)
        self.btn_0 = QPushButton('0', self)
        self.btn_clear = QPushButton('C', self)
        self.btn_add = QPushButton('+', self)
        self.btn_subtract = QPushButton('-', self)
        self.btn_multiply = QPushButton('*', self)
        self.btn_divide = QPushButton('/', self)
        self.btn_equals = QPushButton('=', self)

        # Create the layout
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()

        hbox1.addWidget(self.input_field)

        hbox2.addWidget(self.btn_1)
        hbox2.addWidget(self.btn_2)
        hbox2.addWidget(self.btn_3)
        hbox2.addWidget(self.btn_add)

        hbox3.addWidget(self.btn_4)
        hbox3.addWidget(self.btn_5)
        hbox3.addWidget(self.btn_6)
        hbox3.addWidget(self.btn_subtract)

        hbox4.addWidget(self.btn_7)
        hbox4.addWidget(self.btn_8)
        hbox4.addWidget(self.btn_9)
        hbox4.addWidget(self.btn_multiply)

        hbox5.addWidget(self.btn_clear)
        hbox5.addWidget(self.btn_0)
        hbox5.addWidget(self.btn_equals)
        hbox5.addWidget(self.btn_divide)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        self.setLayout(vbox)

        # Connect the signals to the slots
        self.btn_0.clicked.connect(lambda: self.input('0'))
        self.btn_1.clicked.connect(lambda: self.input('1'))
        self.btn_2.clicked.connect(lambda: self.input('2'))
        self.btn_3.clicked.connect(lambda: self.input('3'))
        self.btn_4.clicked.connect(lambda: self.input('4'))
        self.btn_5.clicked.connect(lambda: self.input('5'))
        self.btn_6.clicked.connect(lambda: self.input('6'))
        self.btn_7.clicked.connect(lambda: self.input('7'))
        self.btn_8.clicked.connect(lambda: self.input('8'))
        self.btn_9.clicked.connect(lambda: self.input('9'))
        self.btn_add.clicked.connect(lambda: self.input('+'))
        self.btn_subtract.clicked.connect(lambda: self.input('-'))
        self.btn_multiply.clicked.connect(lambda: self.input('*'))
        self.btn_divide.clicked.connect(lambda: self.input('/'))
        self.btn_clear.clicked.connect(self.clear)
        self.btn_equals.clicked.connect(self.calculate)

    def input(self, value):
        self.input_field.setText(self.input_field.text() + value)

    def clear(self):
        self.input_field.setText('')

    def calculate(self):
        expression = self.input_field.text()
        try:
            result = eval(expression)
            self.input_field.setText(str(result))
        except:
            self.input_field.setText('Error')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())