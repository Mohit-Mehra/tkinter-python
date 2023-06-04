import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x: {event.x} y : {event.y}')

window = tk.Tk()
window.title("Event Binding")
window.geometry('600x500')

text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text = "Button")
btn.pack()

# Events
btn.bind('<Alt-KeyPress-a>', lambda event:print(event))
window.bind('<Motion>',get_pos)

window.bind('<KeyPress>', lambda event:print(f"Button is pressed ({event.char})"))

entry.bind('<FocusIn>', lambda event:print("Entry Field is Selected"))
entry.bind('<FocusOut>', lambda event:print("Entry Field is unSelected"))

# MouseWheel
text.bind("<Shift-MouseWheel>",lambda event:print("MouseWheel"))


window.mainloop()