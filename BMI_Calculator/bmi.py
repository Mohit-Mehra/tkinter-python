import customtkinter as ctk
from settings import *
from ctypes import windll, byref, sizeof, c_int


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=GREEN)
        self.title('')
        self.iconbitmap('python.ico')
        self.geometry('400x400')
        self.resizable(False, False)
        self.chaange_title_bar_color()

        # Layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

        # Widgets
        RessultText(self)
        WeightInput(self)

        self.mainloop()

    def chaange_title_bar_color(self):
        HWND = windll.user32.GetParent(self.winfo_id())

        title_bar_color = TITILE_HEX_COLOR
        windll.dwmapi.DwmSetWindowAttribute(
            HWND,
            35,
            byref(c_int(title_bar_color)),
            sizeof(c_int)
        )


class RessultText(ctk.CTkLabel):
    def __init__(self, parent):
        font = ctk.CTkFont(family=FONT, size=MAIN_TEXT_SIZE, weight='bold')
        super().__init__(master=parent, text=22.5, font=font, text_color=WHITE)
        self.grid(column=0, row=0, rowspan=2, sticky='nsew')


class WeightInput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(column=0, row=2, sticky='nswe', padx=10, pady=10)

        # Layout
        self.rowconfigure(0, weight=1, uniform='b')
        self.columnconfigure(0, weight=2, uniform='b')
        self.columnconfigure(1, weight=1, uniform='b')
        self.columnconfigure(2, weight=3, uniform='b')
        self.columnconfigure(3, weight=1, uniform='b')
        self.columnconfigure(4, weight=2, uniform='b')

        # Widgets
        font = ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE)
        label = ctk.CTkLabel(self, text="70Kg", text_color=BLACK, font=font)
        label.grid(row=0, column=2)

        # Buttons
        minus_button = ctk.CTkButton(
            self,
            text='-',
            font=font,
            text_color=BLACK,
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
            corner_radius=BUTTON_CORNER_RADIUS
        )
        minus_button.grid(row=0, column=0, sticky='ns', padx=8, pady=8)

        plus_button = ctk.CTkButton(
            self,
            text='+',
            font=font,
            text_color=BLACK,
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
            corner_radius=BUTTON_CORNER_RADIUS
        )
        plus_button.grid(row=0, column=4, sticky='ns', padx=8, pady=8)

        small_minus_button = ctk.CTkButton(
            self,
            text='-',
            font=font,
            text_color=BLACK,
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
            corner_radius=BUTTON_CORNER_RADIUS
        )
        small_minus_button.grid(row=0, column=1, padx=4, pady=4)

        small_plus_button = ctk.CTkButton(
            self,
            text='+',
            font=font,
            text_color=BLACK,
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
            corner_radius=BUTTON_CORNER_RADIUS
        )
        small_plus_button.grid(row=0, column=3, padx=4, pady=4)


if __name__ == "__main__":
    App()
