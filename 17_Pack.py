import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Pack")

# Widgets
label1 = ttk.Label(window, text = "First", background = 'red')
label2 = ttk.Label(window, text = "Second", background = 'blue')
label3 = ttk.Label(window, text = "Third", background = 'green')
button = ttk.Button(window, text = 'Button')

# Layout
# label1.pack(side = 'top', expand = True, fill = 'both')
# label2.pack(side = 'top', fill = 'x')
# label3.pack(side = 'top')
# button.pack(side = 'top', expand = True, fill = 'y')

# Exercise 1
# label1.pack(side = 'top', fill = 'x')
# label2.pack(side = 'top', expand = True)
# label3.pack(side = 'top', expand = True, fill = 'both')
# button.pack(side = 'top', fill = 'x')

# label1.pack(side = 'left', expand = True, fill = 'both')
# label2.pack(side = 'top', expand = True, fill = 'both')
# label3.pack(side = 'top', expand = True, fill = 'both')
# button.pack(side = 'top', expand = True, fill = 'both')

# Exercise 2
label1.pack(side = 'top', expand = True, fill = 'both',padx = 10, pady = 10)
label2.pack(side = 'left', expand = True, fill = 'both')
label3.pack(side = 'top', expand = True, fill = 'both')
button.pack(side = 'top', expand = True, fill = 'both')


window.mainloop()