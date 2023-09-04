import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('400x400')
window.title("Colors")

ttk.Label(window, background='#88f').pack(expand=True, fill='both')
ttk.Label(window, background='#08f').pack(expand=True, fill='both')
ttk.Label(window, background='#0f0').pack(expand=True, fill='both')
ttk.Label(window, background='#E1C16E').pack(expand=True, fill='both')

# Black
ttk.Label(window, background='#000').pack(expand=True, fill='both')

# white
ttk.Label(window, background='#FFF').pack(expand=True, fill='both')

ttk.Label(window, background='#888').pack(expand=True, fill='both')
window.mainloop()
