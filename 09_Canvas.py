import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Canvas")
window.geometry('600x400')

# Canvas
canvas = tk.Canvas(window, bg='white')
canvas.pack()

canvas.create_rectangle((10, 10, 100, 200), fill="purple",
                        width=10, dash=(4, 2, 1, 1), outline="green")
canvas.create_line(0, 0, 100, 150, fill='blue')
canvas.create_oval(200, 10, 100, 100, fill="red")
canvas.create_arc(200, 10, 100, 100, fill="gray",
                  start=45, extent=140)
# canvas.create_polygon(0,0,100,200,300,50,fill="gray")
canvas.create_text(50, 50, text="Hello World", fill="yellow")
canvas.create_window(50, 100, window=ttk.Label(window, text="Text in Canvas"))

# Paint App


def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size / 2, y - brush_size / 2,
                       x + brush_size / 2, y + brush_size / 2),fill='black')

def brush_size_adjust(event):
    global brush_size
    if(event.delta > 0):
        brush_size += 4
    else:
        brush_size -= 4

    brush_size = max(0,min(brush_size,50))

brush_size = 2
canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>',brush_size_adjust)

window.mainloop()
