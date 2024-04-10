import os
import time
import csv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == config_path:
            copy_lines_to_csv(config_path, csv_path)
        elif event.src_path == csv_path:
            copy_lines_to_config(csv_path, config_path)

def copy_lines_to_csv(config_path, csv_path):
    with open(config_path, 'r') as config_file, open(csv_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for line in config_file:
            words = line.split()
            csv_writer.writerow(words)

def copy_lines_to_config(csv_path, config_path):
    with open(csv_path, 'r', newline='') as csv_file, open(config_path, 'w') as config_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            line = ' '.join(row)
            config_file.write(line + '\n')

config_directory = input("Enter the directory containing the config.h file: ")

for file in os.listdir(config_directory):
    if file.lower().endswith("_cfg.h"):
        config_filename = file
        break

config_path = os.path.join(config_directory, config_filename)

csv_directory = input("Enter the directory where you want to create the CSV file: ")
csv_filename = "config_lines.csv"
csv_path = os.path.join(csv_directory, csv_filename)

copy_lines_to_csv(config_path, csv_path)

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path=os.path.dirname(config_path), recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
        continue_monitoring = input("Do you want to continue monitoring? (yes/no): ")
        if continue_monitoring.lower() == 'no':
            break
except KeyboardInterrupt:
    pass
finally:
    observer.stop()
    observer.join()