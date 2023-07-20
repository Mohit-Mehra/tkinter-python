import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Grid")

# Widgets
label1 = ttk.Label(window, text="First", background='red')
label2 = ttk.Label(window, text="Second", background='blue')
label3 = ttk.Label(window, text="Third", background='green')
label4 = ttk.Label(window, text="Third", background='orange')
button1 = ttk.Button(window, text='Button 1')
button2 = ttk.Button(window, text='Button 2')
entry = ttk.Entry(window)

# Define a grid
window.columnconfigure((0, 1, 2), weight=1, uniform='a')
window.columnconfigure(3, weight=2, uniform='a')
window.rowconfigure(0, weight=1, uniform='a')
window.rowconfigure(1, weight=1, uniform='a')
window.rowconfigure(2, weight=1, uniform='a')
window.rowconfigure(3, weight=3, uniform='a')

# Pace Widgets
label1.grid(row=0, column=0, sticky='nsew')
label2.grid(row=1, column=1, rowspan=3, sticky='nsew')
label3.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=20, pady=10)
label4.grid(row=3, column=3, sticky='se')

# Excercise
button1.grid(row=0, column=3, sticky='nsew')
button2.grid(row=2, column=2, sticky='nsew')
entry.grid(row=3, column=3)


window.mainloop()
