import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("400x500")

# Widgets
label1 = ttk.Label(window, text="First", background='skyblue')
label2 = ttk.Label(window, text="Second", background='cyan')

# label1.lift()
# label2.lower()

button1 = ttk.Button(window, text='raise Label 1',
                     command=lambda: label1.tkraise())
button2 = ttk.Button(window, text='raise label 2',
                     command=lambda: label2.tkraise())

label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)

button1.place(relx=0.8, rely=1, anchor='se')
button2.place(relx=1, rely=1, anchor='se')

window.mainloop()
