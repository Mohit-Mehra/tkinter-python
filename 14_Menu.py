import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Menu")

# Menu
menu = tk.Menu(window)

# Sub Menu
file_menu = tk.Menu(menu, tearoff = False)
file_menu.add_command(label = "New", command = lambda: print("New File"))
file_menu.add_command(label = "Open", command = lambda: print("Open File"))
file_menu.add_separator()
file_menu.add_command(label = "Save", command = lambda: print("Save File"))
menu.add_cascade(label="File", menu = file_menu)

# Other Sub Menu
help_menu = tk.Menu(menu, tearoff = False)
menu.add_cascade(label = "Help", menu = help_menu)
help_menu.add_command(label = "Help", command = lambda: print(help_check_String.get()))
help_check_String = tk.StringVar()
help_menu.add_checkbutton(label  = "check",onvalue = "on", offvalue = 'off', variable = help_check_String)

window.configure(menu = menu)

# Menu Button
menu_Button = ttk.Menubutton(window,text = "Menu Button")
menu_Button.pack()

button_sub_menu = tk.Menu(menu_Button, tearoff = False)
button_sub_menu.add_command(label = "Test", command = lambda: print("Test"))
button_sub_menu.add_checkbutton(label = "Check")
menu_Button.configure(menu = button_sub_menu)

window.mainloop()
