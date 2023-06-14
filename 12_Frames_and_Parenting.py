import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Frames and Parenting")

# frames
frame = ttk.Frame(window, width = 100, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side = 'left')

# master setiing
label = ttk.Label(frame, text = "Hello World")
label.pack()

button = ttk.Button(frame, text = "Click Me")
button.pack()

# Example
label2 = ttk.Label(window, text = "Outside frame")
label2.pack(side = 'left')

window.mainloop()