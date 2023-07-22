import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x600")
window.title("Combined Layout")
window.minsize(600, 600)

# Main Layout Widgets
menu_frame = ttk.Frame(window)
main_frame = ttk.Frame(window)

# main Place Layout
menu_frame.place(x=0, y=0, relwidth=0.3, relheight=1)
main_frame.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

# Menu Widgets
menu_button1 = ttk.Button(menu_frame, text="Button 1")
menu_button2 = ttk.Button(menu_frame, text="Button 2")
menu_button3 = ttk.Button(menu_frame, text="Button 3")

menu_Slider1 = ttk.Scale(menu_frame, orient='vertical')
menu_Slider2 = ttk.Scale(menu_frame, orient='vertical')

toggle_frame = ttk.Frame(menu_frame)
menu_toggle1 = ttk.Checkbutton(toggle_frame, text='Check 1')
menu_toggle2 = ttk.Checkbutton(toggle_frame, text='Check 2')

# ttk.Label(menu_frame, background="red").pack(expand=True, fill='both')
# ttk.Label(main_frame, background="cyan").pack(expand=True, fill='both')

window.mainloop()
