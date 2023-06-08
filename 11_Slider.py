import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title("Slider")

# Slider
scale_float = tk.DoubleVar(value = 15)
scale = ttk.Scale(window, 
                  command = lambda value:bar.stop(), 
                  from_ = 0, 
                  to = 25,
                  length = 300, 
                  orient='vertical',
                  variable = scale_float)
scale.pack()

# Progress Bar
bar = ttk.Progressbar(window,
                      variable = scale_float,
                      maximum = 25,
                      orient = 'horizontal',
                      mode = 'indeterminate',
                      length = 400)
bar.pack()
bar.start(1000)

# Scrolledtext
scrolled_text = scrolledtext.ScrolledText(
    window,
    width = 100,
    height = 3
)
scrolled_text.pack()



window.mainloop()