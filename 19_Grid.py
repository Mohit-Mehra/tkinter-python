import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Grid")

# Widgets
label1 = ttk.Label(window, text = "First", background = 'red')
label2 = ttk.Label(window, text = "Second", background = 'blue')
label3 = ttk.Label(window, text = "Third", background = 'green')
label4 = ttk.Label(window, text = "Third", background = 'orange')
button1 = ttk.Button(window, text = 'Button 1')
button2 = ttk.Button(window, text = 'Button 2')
entry = ttk.Entry(window)

# Define a grid
window.columnconfigure((0,1,2), weight = 1)
window.columnconfigure(3, weight = 10)
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 1)
window.rowconfigure(3, weight = 3)

# Pace Widgets
label1.grid(row = 0, column = 0, sticky = 'nsew')
label2.grid(row = 0, column = 1,sticky = 'w')
label3.grid(row = 0, column = 3,sticky = 'ew')

window.mainloop()