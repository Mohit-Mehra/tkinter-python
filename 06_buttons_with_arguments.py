import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
    print("Button is pressed")
    print(entry_string.get())

def outer_func(parameter):
    def inner_func():
        print("Button is Pressed")
        print(parameter.get())
    return inner_func

window = tk.Tk()
window.title("Buttons With Arguments")
window.geometry('600x400')

entry_string = tk.StringVar(value = "Test")
entry = ttk.Entry(window, textvariable=entry_string).pack()

button = ttk.Button(window, text = "Button", command= lambda : button_func(entry_string)).pack()

button2 = ttk.Button(window, text = "Button 2 ", command= outer_func(entry_string)).pack()

window.mainloop()