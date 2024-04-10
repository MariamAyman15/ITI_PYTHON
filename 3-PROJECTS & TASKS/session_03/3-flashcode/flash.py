'''import subprocess

# Set the path to the avrdude executable
avrdude_path = "C:\ES\Proteus 8 Professional\BIN"

# Set the path to the hex file that contains the code to be flashed
hex_file = "test.hex"

# Set the parameters for avrdude
mcu = "atmega328p"  # the AVR microcontroller used in the Proteus simulation
port = "COM1"       # the serial port used by the Proteus simulation
baudrate = "115200" # the baud rate used by the Proteus simulation

# Construct the avrdude command
cmd = [avrdude_path, "-c", "arduino", "-p", mcu, "-P", port, "-b", baudrate, "-U", "flash:w:" + hex_file]

# Run the avrdude command
result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Print the output of the avrdude command
print(result.stdout.decode("utf-8"))
print(result.stderr.decode("utf-8"))'''

import win32com.client

# Load Proteus COM interface
win32com.client.pythoncom.CoInitialize()

# Create a new instance of the Proteus application
app = win32com.client.Dispatch("Proteus.Application")

# Open the desired Proteus project file
app.LoadNetlist("G:\ES\LINUX\1-PYTHON\3-PROJECTS & TASKS\session_03\3-flashcode")

# Get a reference to the microcontroller in the Proteus project
mcu = app.Design.Components("MCU")

# Load the hex file onto the microcontroller
mcu.LoadHex("G:\ES\LINUX\1-PYTHON\3-PROJECTS & TASKS\session_03\3-flashcode")

# Release all allocated