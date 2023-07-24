import tkinter as tk
from tkinter import ttk

# Function
def create_segment(parent, label_text, button_text):
    frame = ttk.Frame(master=parent)

    frame.rowconfigure(0, weight=1)
    frame.columnconfigure((0, 1, 2), uniform='a', weight=1)
    ttk.Label(frame, text=label_text).grid(row=0, column=0, sticky='news')
    ttk.Button(frame, text=button_text).grid(row=0, column=1, sticky='news')

    return frame

# Class
class Segment(ttk.Frame):
    def __init__(self, parent, label_text, Button_text):
        super().__init__(master=parent)

        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), uniform='a', weight=1)
        ttk.Label(self, text=label_text).grid(row=0, column=0, sticky='news')
        ttk.Button(self, text=Button_text).grid(row=0, column=1, sticky='news')

        self.pack(expand=True, fill='both', padx=10, pady=10)


window = tk.Tk()
window.geometry("400x600")
window.title("Widgets and Return")

# Widgets
Segment(window, 'Label', 'Button')
Segment(window, 'Yo', 'Click')
Segment(window, 'Test', 'test')
Segment(window, 'Test', 'test')

create_segment(window, 'Label', 'Button').pack(expand=True, fill='both', padx=10, pady=10)
create_segment(window, 'Yo', 'Click').pack(expand=True, fill='both', padx=10, pady=10)
create_segment(window, 'Test', 'test').pack(expand=True, fill='both', padx=10, pady=10)


window.mainloop()
