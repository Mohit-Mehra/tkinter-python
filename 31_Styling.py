import tkinter as tk
from tkinter import ttk, font

window = tk.Tk()
window.geometry('400x400')
window.title("Multiple Windows")

# print(font.families())

style = ttk.Style()
# print(style.theme_names())
# style.theme_use('winnative')

style.configure('new.TButton', foreground='green', font=('Jokerman', 30))
style.map('new.Tbutton', foreground=[('pressed','red'),('disabled','yellow')])

label = ttk.Label(window,
                  text='Label\n And another Line',
                  background='cyan',
                  foreground='green',
                  font=('Jokerman', 30),
                  justify='right')
label.pack()

button = ttk.Button(window, text='Button', style='new.TButton')
button.pack()

window.mainloop()
