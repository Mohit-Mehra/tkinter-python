import customtkinter as ctk
from PIL import Image
from os import walk


class AnimatedButton(ctk.CTkButton):
    def __init__(self, parent, light_path, dark_path):
        self.import_folders(light_path, dark_path)

        super().__init__(master=parent, text='Animated Button')
        self.pack(expand=True)

    def import_folders(self, light_path, dark_path):
        for path in (light_path, dark_path):
            for _, __, image_data in walk(path):
                # print(image_data.split('.'[0][-5:]))
                sorted_data = sorted(
                    image_data,
                    key=lambda item: (item.split('.'[0][-5:]))
                )
                full_path = 


window = ctk.CTk()
window.title('Image Animation')
window.geometry('300x200')

AnimatedButton(window, 'black', 'yellow')

window.mainloop()
