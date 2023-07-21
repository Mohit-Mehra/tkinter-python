import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("400x600")

# Widgets
label1 = ttk.Label(window, text="First", background='red')
label2 = ttk.Label(window, text="Second", background='cyan', width=50)

# label1.pack()
# label2.pack()

window.columnconfigure((0, 1), weight=1, uniform='a')
window.rowconfigure((0, 1), weight=1, uniform='a')

label1.grid(row=0, column=0)
label2.grid(row=1, column=0, sticky="news")

window.mainloop()
