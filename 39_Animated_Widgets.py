import customtkinter as ctk
from random import choice


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent, fg_color='cyan')

        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = abs(start_pos - end_pos)

        self.pos = start_pos
        self.in_start_pos = True

        self.place(
            relx=self.start_pos,
            rely=0,
            relwidth=self.width,
            relheight=1
        )

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backword()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(
                relx=self.pos,
                rely=0,
                relwidth=self.width,
                relheight=1
            )
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backword(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(
                relx=self.pos,
                rely=0,
                relwidth=self.width,
                relheight=1
            )
            self.after(10, self.animate_backword)
        else:
            self.in_start_pos = True


def move_btn():
    global button_x
    button_x += 0.001
    button.place(relx=button_x, rely=0.5, anchor="center")
    if button_x < 0.9:
        window.after(10, move_btn)

    # colors = ["red", 'yellow', 'pink', 'green', 'cyan', 'white']
    # color = choice(colors)
    # button.configure(fg_color=color)


def infinite_print():
    global button_x
    button_x += 0.5
    if (button_x < 10):
        print('infinte')
        print(button_x)
        window.after(100, infinite_print)


window = ctk.CTk()
window.title("Animated Widgets")
window.geometry('600x400')

animated_panel = SlidePanel(window, 0, -0.3)

button_x = 0.5
button = ctk.CTkButton(window,
                       text="Toogle sidebar",
                       command=animated_panel.animate
                       )
button.place(relx=button_x, rely=0.5, anchor="center")

window.mainloop()
