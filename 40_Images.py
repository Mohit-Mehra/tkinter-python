import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

# window
window = tk.Tk()
window.title('Images')
window.geometry('600x400')

# import images
image_original = Image.open('4345.jpg')
image_tk = ImageTk.PhotoImage(image_original)

itachi = Image.open('12649.jpg').resize((30, 30))
itachi_Tk = ImageTk.PhotoImage(itachi)

# label = ttk.Label(window, text='Goku', image=image_tk)
# label.pack()

button = ttk.Button(window, text="Button", image=itachi_Tk, compound='right')
button.pack()

window.mainloop()
