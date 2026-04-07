import subprocess

def get_active_window():
    try:
        window = subprocess.check_output(
            "xdotool getactivewindow getwindowname",
            shell=True
        )
        return window.decode().strip()
    except:
        return "Unknown"
