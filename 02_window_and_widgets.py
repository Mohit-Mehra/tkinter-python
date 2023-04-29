import tkinter as tk
from tkinter import ttk

def button_func():
    print("Button Pressed! ")

# create a window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry('800x500')

# ttk label
label = ttk.Label(master = window, text = 'test')
label.pack()

# tk text 
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# new label
new_label = ttk.Label(master=window, text='My Label')
new_label.pack()

# ttk button
button = tk.Button(master = window, text = 'Button', command = button_func)
button.pack()

# run
window.mainloop()