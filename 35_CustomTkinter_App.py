import customtkinter as ctk
# import tkinter as tk
# from tkinter import ttk


class App(ctk.CTk):
    def __init__(self, title, size):
        # Mian Setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        # Widgets
        self.menu = Menu(self)
        self.main = Main(self)

        self.mainloop()


class Menu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=0.3, relheight=1)
        self.create_widgets()

    def create_widgets(self):
        menu_button1 = ctk.CTkButton(self, text="Button 1")
        menu_button2 = ctk.CTkButton(self, text="Button 2")
        menu_button3 = ctk.CTkButton(self, text="Button 3")

        menu_Slider1 = ctk.CTkSlider(self, orientation='vertical')
        menu_Slider2 = ctk.CTkSlider(self, orientation='vertical')

        toggle_frame = ctk.CTkFrame(self)
        menu_toggle1 = ctk.CTkCheckBox(toggle_frame, text='Check 1')
        menu_toggle2 = ctk.CTkCheckBox(toggle_frame, text='Check 2')

        entry = ctk.CTkEntry(self)

        # Create a Grid
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

        menu_button1.grid(row=0, column=0, sticky='news', columnspan=2)
        menu_button2.grid(row=0, column=2, sticky='news')
        menu_button3.grid(row=1, column=0, sticky='news', columnspan=3)

        menu_Slider1.grid(row=2, column=0, rowspan=2,
                          sticky="ns", pady=20)
        menu_Slider2.grid(row=2, column=2, rowspan=2,
                          sticky="ns", pady=20)

        # Toggle Layout
        toggle_frame.grid(row=4, column=0, columnspan=3, sticky="news")
        menu_toggle1.pack(side='left', expand=True)
        menu_toggle2.pack(side='left', expand=True)

        # Entry Layout
        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor='center')


class Main(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

        frame = ctk.CTkFrame(self)
        label = ctk.CTkLabel(frame, text='Test 1')
        button = ctk.CTkButton(frame, text='Button')

        label.pack(expand=True, fill="both")
        button.pack(expand=True, fill="both", pady=10)
        frame.pack(side="left", expand=True, fill='both')


App('Class based App with CTk', (600, 600))
