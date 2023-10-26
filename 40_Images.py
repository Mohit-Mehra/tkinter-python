import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk


def stretch_image(event):

    global resized_tk
    # size
    width = event.width
    height = event.height

    # Create an Image
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    # place on yje canvas
    canvas.create_image(0, 0, image=resized_tk, anchor='nw')


# def fill_image(event):
#     global resized_tk

#     # current ratio of the event
#     canvas_ratio = event.width / event.height

#     # get Coordinates
#     if canvas_ratio > image_ratio:
#         width = int(event.width)
#         height = int(width / image_ratio)
#     else:
#         width = 1
#         height = 1

#     resized_image = image_original.resize((width, height))
#     resized_tk = ImageTk.PhotoImage(resized_image)
#     canvas.create_image(int(event.width/2),
#                         int(event.height/2), anchor="center", image=resized_tk)


# window
window = tk.Tk()
window.title('Images')
window.geometry('600x400')

# Grid
window.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
window.rowconfigure(0, weight=1)

# import images
image_original = Image.open('4345.jpg')
# image_ratio = image_original.size[0] / image_original[1]
image_tk = ImageTk.PhotoImage(image_original)

itachi = Image.open('12649.jpg').resize((30, 30))
itachi_Tk = ImageTk.PhotoImage(itachi)

image_ctk = ctk.CTkImage(
    light_image=Image.open('12751.jpg'),
    dark_image=Image.open("12751.jpg")
)

# label = ttk.Label(window, text='Goku', image=image_tk)
# label.pack()
button_frame = ttk.Frame(window)
button = ttk.Button(button_frame, text="Button",
                    image=itachi_Tk, compound='right')
button.pack(pady=10)

button_ctk = ctk.CTkButton(button_frame, text="Button",
                           image=image_ctk, compound='right')
button_ctk.pack(pady=10)

button_frame.grid(column=0, row=0, sticky='nsew')

canvas = tk.Canvas(window, bd=0, highlightthickness=0, relief='ridge')
canvas.grid(column=1, columnspan=3, row=0, sticky='news')
# canvas.create_image(0, 0, image=image_tk, anchor="nw")

canvas.bind("<Configure>", stretch_image)
# canvas.bind("<Configure>", fill_image)

window.mainloop()
