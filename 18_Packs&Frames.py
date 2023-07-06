import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Pack and Frames")

# Top Frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text = "First", background = 'red')
label2 = ttk.Label(top_frame, text = "Second", background = 'blue')

label3 = ttk.Label(window, text = "Third", background = 'green')
label4 = ttk.Label(window, text = "Fourth", background = 'orange')
button1 = ttk.Button(window, text = 'Button1')
button2 = ttk.Button(window, text = 'Button2')

# Top Layout
label1.pack(fill = 'both', expand = True)
label2.pack(fill = 'both', expand = True)
top_frame.pack(fill = 'both', expand = True)

window.mainloop()