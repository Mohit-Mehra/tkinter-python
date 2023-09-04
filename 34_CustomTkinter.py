import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# window
window = ctk.CTk()
window.title('CustomTkinter App')
window.geometry('600x400')

# Widgets
string = ctk.StringVar(value='Custom String')
label = ctk.CTkLabel(window, text="Label", fg_color=('cyan', 'blue'),
                     text_color=('red', 'green'), corner_radius=10, textvariable=string)
label.pack()

button = ctk.CTkButton(window, text="Button",
                       fg_color='#FF0', text_color='#000', hover_color='#AA0', command=lambda: ctk.set_appearance_mode('light'))
button.pack()

frame = ctk.CTkFrame(window, fg_color='transparent')
frame.pack()

slider = ctk.CTkSlider(frame)
slider.pack(padx=20, pady=20)

# Exercise Switch
switch = ctk.CTkSwitch(window, text='Exercise Switch',
                       fg_color=('blue', 'red'), progress_color='pink',
                       button_color='green', button_hover_color='yellow',
                       switch_width=60, switch_height=30,
                       corner_radius=2)
switch.pack()

window.mainloop()
