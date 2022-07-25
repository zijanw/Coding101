import tkinter as tk
from ctypes import windll

## display a window

# main window in Tkinter is called root by convention
root = tk.Tk()  

# place a label on the root window
message = tk.Label(root, text = "Hello, world!")
message.pack()

# make app run across windows, linux, macOS
try:
    # fixing the blur UI 
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)


finally:
    # mainloop() keeps window on the screen
# typically calling it as the last statement after creating all widgets(components)
    root.mainloop()