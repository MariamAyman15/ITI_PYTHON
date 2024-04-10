import subprocess   
import os

# List all files with the ".txt" extension in the current directory
txt_files = [f for f in os.listdir(".") if f.endswith(".c")]
print(txt_files)

# Compile the C files
result =subprocess.run(['avr-gcc', '-mmcu=atmega32', '-Os', '-c', 'main.c', '-o', 'main.o'])

result =subprocess.run(['avr-gcc', '-mmcu=atmega32', '-Os', '-c', 'DIO_prg.c', '-o', 'DIO_prg.o'])

result =subprocess.run(['avr-gcc', '-mmcu=atmega32', '-Os', '-c', 'LED_prg.c', '-o', 'LED_prg.o'])

# Link the object files
result =subprocess.run(['avr-gcc', '-mmcu=atmega32', '-Os', 'main.o', 'DIO_prg.o','LED_prg.o' ,'-o','output.elf'])

# Generate the hex file
result =subprocess.run(['avr-objcopy', '-O', 'ihex', '-R', '.eeprom', 'output.elf', 'output.hex'])