# lesson from https://www.pythontutorial.net/tkinter/

import tkinter as tk
from tkinter import ttk # tkinter themed widgets
from ctypes import windll

### display a window

## main window in Tkinter is called root by convention
root = tk.Tk() 

## change window title
root.title("HEHEHE")

## to center the app in the screen
# window dimension
window_width = 800
window_height = 600

# screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point of the screen
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

## width[x]height[+-]x[+-]y
# from: https://www.pythontutorial.net/tkinter/tkinter-window/
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

## make window mixed size
# root.resizable(False, False)

## window max & min resizable size
root.minsize(400, 300)
root.maxsize(1600, 1200)

## window transparency
# 0.0: fully transparent
# 1.0: fully opaque
# window.attributes('-alpha', transparency)
root.attributes('-alpha', 1)

## make window always on top
# window.attributes('-topmost', 1)
root.attributes('-topmost', 1)

## to move window up
# window.lift()
# window.lift(another_window)

## to move window down
# window.lower()
# window.lower(another_window)

## to change icon of window
# must be accessible .ico file
# window.iconbitmap("./path/to/file/name.ico")
root.iconbitmap("./what.ico")

def button_clicked():
    print("Button clicked")

button = ttk.Button(root, text='Click Me',command=button_clicked)
button.pack()
## place a label on the root window
ttk.Label(root, text = "Hello, world!").pack()

## make app run across windows, linux, macOS
try:
    ## fixing the blur UI 
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)


finally:
    ## mainloop() keeps window on the screen
    # typically calling it as the last statement after creating all widgets(components)
    root.mainloop()