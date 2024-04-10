import sys
import os 
import subprocess
from PyQt5.QtWidgets import QApplication , QPushButton , QWidget ,QLabel
from PyQt5.QtGui import QIcon

def func():
    # List all files with the ".txt" extension in the current directory
    txt_files = [f for f in os.listdir(".") if f.endswith(".c")]
    print(txt_files)

    # Compile the C files
    result =subprocess.run(['avr-gcc', '-mmcu=atmega32', '-Os', '-c', 'main.c', '-o', 'main.o'])
    result =subprocess.run(['avr-gcc', '-mmcu=atmega32', '-Os', '-c', 'DIO_program.c', '-o', 'DIO_program.o'])
    result =subprocess.run(['avr-gcc', '-mmcu=atmega32', '-Os', '-c', 'LED_program.c', '-o', 'LED_program.o'])

    # Link the object files
    result =subprocess.run(['avr-gcc', '-mmcu=atmega32', '-Os', 'main.o', 'DIO_program.o','LED_program.o', '-o', 'output.elf'])

    # Generate the hex file
    result =subprocess.run(['avr-objcopy', '-O', 'ihex', '-R', '.eeprom', 'output.elf', 'output.hex'])
a=QApplication(sys.argv)

root = QWidget()
root.setWindowTitle("Compile Your Code")
root.setGeometry(300,400,100,100)

Button=QPushButton("Compile",root)
Button.pressed.connect(func)
Button.setGeometry(50,50,100,50)
Button.setIcon(QIcon("logo.png"))
L =QLabel("Mohamed Elfawakhry",root)
L.setGeometry(50,100,200,200)
root.show()
sys.exit(a.exec_())