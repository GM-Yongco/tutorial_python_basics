import time


from win32 import win32gui
from win32.lib.win32con import *

time.sleep(5)
print("starting")
# su.spotify_play()

def enum_windows_callback(hwnd, extra):
    # This function will be called for each window enumerated by EnumWindows.
    # 'hwnd' is the window handle, and 'extra' is any extra data you pass to EnumWindows.

    # Get the window text (title) and class name for each window
    window_text = win32gui.GetWindowText(hwnd)
    window_class = win32gui.GetClassName(hwnd)

    # Print or process the window information (you can modify this as needed)
    print(f"Window Handle: {hwnd:10}, Title: {window_text:50}, Class: {window_class}")

def enum_windows():
    # Call EnumWindows with the callback function enum_windows_callback
    # The second argument (extra) can be used to pass extra data to the callback if needed (set to None in this example).
    win32gui.EnumWindows(enum_windows_callback, None)

enum_windows()