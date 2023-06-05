import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("ComboBox And SpinBox")
window.geometry('600x500')

# ComboBox
items = ("Hello","World","Python")
string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window,textvariable=string)
# combo['values'] = items
combo.config(values = items)
combo.pack()

# Events
combo.bind('<<ComboboxSelected>>',lambda event:combo_label.config(text = f"Selected Value: {string.get()}"))

combo_label = ttk.Label(window, text="Label")
combo_label.pack()

# SpinBox
integer = tk.IntVar(value = 12)
spin = ttk.Spinbox(window,from_ = 1,to = 20, increment=2,command = lambda:print(integer.get()),textvariable=integer)
spin.bind("<<Increment>>",lambda event:print("Up"))
spin.bind("<<Decrement>>",lambda event :print("Down"))
# spin['values'] = (1,23,4,5)
spin.pack()


# ABCD spinbox
letters = ("A","B","C","D")
l_string = tk.StringVar(value = letters[0])
l_spin = ttk.Spinbox(window,textvariable=l_string)
l_spin.pack()

window.mainloop()