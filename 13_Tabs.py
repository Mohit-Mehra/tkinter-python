import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Tabs")

# Notebook widget
notebook = ttk.Notebook(window)

tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1,text="Text for tab1")
label1.pack()
button1 = ttk.Button(tab1,text="Button")
button1.pack()

tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2,text = "Text in lab2")
label2.pack()
entry = ttk.Entry(tab2)
entry.pack()

# Exercise
tab3 = ttk.Frame(notebook)
button = ttk.Button(tab3,text = "button")
button.pack()


notebook.add(tab1,text = "Tab1")
notebook.add(tab2,text = "Tab2")
notebook.add(tab3,text = "Tab3")
notebook.pack()


window.mainloop()