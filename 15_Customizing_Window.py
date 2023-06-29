import tkinter as tk
from tkinter import ttk

window = tk.Tk()
# window.geometry("600x400+100+200")
window.title("Customizing Window")
window.iconbitmap("python.ico")

# Exercice window in the middle of screen
window_width = 900
window_height = 500
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

left = int(display_width / 2 - window_width / 2)
top = int(display_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')


# Window Sizes
window.minsize(200,100)
# window.maxsize(800,700)
window.resizable(True,False)

# Screen Attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# Window Attributes
window.attributes('-alpha',1)
# window.attributes('-topmost',True)

# Security Event
window.bind("<Escape>",lambda event:window.quit())
# window.attributes('-disabled',True)
# window.attributes('-fullscreen',True)

# Title Bar
# window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx=1.0,rely=1.0,anchor='se')

window.mainloop()