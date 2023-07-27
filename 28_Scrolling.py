import tkinter as tk
from tkinter import ttk
from random import randint, choice

window = tk.Tk()
window.geometry("600x400")
window.title("Scrolling")

# Canvas
# canvas = tk.Canvas(window, bg='white', scrollregion=(0, 0, 2000, 5000))
# canvas.create_line(0, 0, 2000, 5000, fill='green', width=10)
# for i in range(100):
#     l = randint(0, 2000)
#     t = randint(0, 5000)
#     r = l + randint(10, 500)
#     b = t + randint(10, 500)
#     color = choice(("cyan", "blue", "pink", 'purple'))
#     canvas.create_rectangle(l, t, r, b, fill=color)
# canvas.pack(fill='both', expand=True)

# # mousewheel Scrolling
# canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(
#     -int(event.delta / 60), "units"))

# # ScrollBar
# scrollBar = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
# canvas.configure(yscrollcommand=scrollBar.set)
# scrollBar.place(relx=1, rely=0, relheight=1, anchor='ne')

# # Create a Horizontal ScrollBar
# scrollBar_Buttom = ttk.Scrollbar(window, orient='horizontal', command=canvas.xview)
# canvas.configure(xscrollcommand = scrollBar_Buttom.set)
# scrollBar_Buttom.place(relx=0,rely=1,relwidth=1,anchor='sw')

# canvas.bind('<Control MouseWheel>', lambda event: canvas.xview_scroll(-int(event.delta / 60), "units"))


# Text
text = tk.Text(window)
for i in range(1,200):
    text.insert(f'{i}.0',f'text:{i} \n')
text.pack(expand=True, fill='both')

# Scroll Text
scrollBar_text = ttk.Scrollbar(window, orient='vertical', command=text.yview)
text.configure(yscrollcommand=scrollBar_text.set)
scrollBar_text.place(relx=1, rely=0, relheight=1, anchor='ne')


window.mainloop()
