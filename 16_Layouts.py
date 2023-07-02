import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Layouts")

# Widgets
label1 = tk.Label(window, text='Label1', background='red')
label2 = tk.Label(window, text='Label2', background='blue')

# # Pack
# label1.pack(side='left', expand=True, fill='x')
# label2.pack(side='bottom', expand=True, fill="both")

# # Grid
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)

# label1.grid(row=0, column=1, sticky='nsew')
# label2.grid(row=1, column=1, columnspan=2, sticky='nsew')

# Place
label1.place(x=100, y=200, width=200, height=100)
label2.place(relx=0.5,rely=0.5,relwidth=1,anchor='e')


window.mainloop()
