import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("400x500")
window.title("Hide Widgets")

# Place
def toggle_label_place():
    global label_visibe
    if label_visibe:
        label.place_forget()
        label_visibe = False
    else:
        label_visibe = True
        label.place(relx=0.5, rely=0.5, anchor='center')


button = ttk.Button(window, text="Toogle Label", command=toggle_label_place)
button.place(x=10, y=10)

label_visibe = True

label = ttk.Label(window, text="A Label")
label.place(relx=0.5, rely=0.5, anchor='center')

window.mainloop()
