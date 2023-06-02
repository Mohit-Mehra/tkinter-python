import tkinter as tk
from tkinter import ttk

def button_func():
    print(stringVar.get())

window = tk.Tk()
window.title("Tkinter Variable")

# String variable
stringVar = tk.StringVar(value = 'start value')

label = ttk.Label(master = window, text = 'label', textvariable = stringVar)
label.pack()

entry = ttk.Entry(master = window, textvariable=stringVar).pack()

button = ttk.Button(master = window, text='button', command=button_func).pack()

integerVar = tk.IntVar(value=5)
label2 = ttk.Label(master = window, text = 'label', textvariable = integerVar)
label2.pack()

entry2 = ttk.Entry(master = window, textvariable=integerVar).pack()

entry3 = ttk.Entry(master = window, textvariable=integerVar).pack()


window.mainloop()