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
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.rowconfigure(0, weight = 1)

# Pace Widgets
label1.grid(row = 0, column = 0, sticky = 'w')
label2.grid(row = 0, column = 1,sticky = 'e')

window.mainloop()