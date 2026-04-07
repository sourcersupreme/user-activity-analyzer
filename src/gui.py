import tkinter as tk
from logger import start_listener, stop_listener

listener = None

def start():
    global listener
    listener = start_listener(update_text)
    status_label.config(text="Status: Running")

def stop():
    stop_listener()
    status_label.config(text="Status: Stopped")

def update_text(log):
    text_box.insert(tk.END, log)
    text_box.see(tk.END)

def create_gui():
    root = tk.Tk()
    root.title("User Activity Monitor")

    global text_box, status_label

    text_box = tk.Text(root, height=20, width=80)
    text_box.pack()

    start_btn = tk.Button(root, text="Start", command=start)
    start_btn.pack()

    stop_btn = tk.Button(root, text="Stop", command=stop)
    stop_btn.pack()

    status_label = tk.Label(root, text="Status: Stopped")
    status_label.pack()

    root.mainloop()
