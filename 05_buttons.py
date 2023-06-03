import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Buttons")
window.geometry('600x400')

def button_func():
    print("Simple Button")
    

button_string = tk.StringVar(value="Simple Button")
button = ttk.Button(window, text = "Simple Button", command= button_func,textvariable=button_string)
button.pack()

# Check Button
check_var = tk.IntVar()
check =ttk.Checkbutton(window, 
                       text = "checkbox 1", 
                       command=lambda:print(check_var.get()),
                       variable = check_var,
                       onvalue=10,
                       offvalue=5
                       ).pack()

# Radio Button
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text = "Radio 1",
    value = "radio1" ,
    variable = radio_var,
    command = lambda:print(radio_var.get())
).pack()
radio2 = ttk.Radiobutton(
    window,
    text = "Radio 2",
    value = 0,
    variable = radio_var
).pack()

window.mainloop()