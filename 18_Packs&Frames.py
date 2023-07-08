import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Pack and Frames")

# Top Frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text = "First", background = 'red')
label2 = ttk.Label(top_frame, text = "Second", background = 'blue')
# Middle Frame
label3 = ttk.Label(window, text = "Third", background = 'green')

# Bottom Frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text = "Fourth", background = 'orange')
button1 = ttk.Button(bottom_frame, text = 'Button1')
button2 = ttk.Button(bottom_frame, text = 'Button2')

# Top Layout
label1.pack(side = "left", fill = 'both', expand = True)
label2.pack(side = "left", fill = 'both', expand = True)
top_frame.pack(fill = 'both', expand = True)

# Middle Layout
label3.pack(expand=True)

# More Widgets
frame = ttk.Frame(bottom_frame)
button3 = ttk.Button(frame,text="Button 3")
button4 = ttk.Button(frame,text="Button 4")
button5 = ttk.Button(frame,text="Button 5")

# Bottom Layout
button1.pack(side = "left",expand=True,fill = 'both')
button2.pack(side = "left",expand=True,fill = 'both')
label4.pack(side = "left",expand=True,fill = 'both')
bottom_frame.pack(expand=True,fill = 'both',padx=20,pady=20)


button3.pack(expand=True,fill = 'both')
button4.pack(expand=True,fill = 'both')
button5.pack(expand=True,fill = 'both')
frame.pack(side='left',fill='both',expand=True)


window.mainloop()