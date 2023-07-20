import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("400x600")
window.title("Place")

# Widgets
label1 = ttk.Label(window, text="First", background='red')
label2 = ttk.Label(window, text="Second", background='blue')
label3 = ttk.Label(window, text="Third", background='green')
button = ttk.Button(window, text='Button 1')

# Layout
label1.place(x=300, y=100, width=100, height=200)
label2.place(relx=0.2, rely=0.1, relwidth=0.4, relheight=0.5)
label3.place(x=80, y=60, width=160, height=300)
button.place(relx=1, rely=1, anchor='center')

frame = ttk.Frame(window)
frame_label = ttk.Label(frame, text="Frame label", background="orange")
frame_button = ttk.Button(frame, text="Frame Button")

# Frame Layout
frame.place(relx=0, rely=0, relwidth=0.2, relheight=1)
frame_label.place(relx=0, rely=0, relwidth=1, relheight=0.5)
frame_button.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# exercise
# Create a label and place it right in the center of the window
# the label should  be half as wide as the window and be 200px tall
e_label = ttk.Label(window, text="Exercise Label", background="yellow")
e_label.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5, height=200)

window.mainloop()
