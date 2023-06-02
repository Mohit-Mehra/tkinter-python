import tkinter as tk
from tkinter import ttk

def button_func():
    entry_text = entry.get()

    # label.config(text = "Some Other text")
    label['text'] = entry_text
    # entry["state"] = 'disabled'
    print(label.config())

# window
window = tk.Tk()
window.title("Setting Widgets")

# widgets
label = ttk.Label(master=window, text='Text')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window,text="Button", command=button_func)
button.pack()

# run
window.mainloop()