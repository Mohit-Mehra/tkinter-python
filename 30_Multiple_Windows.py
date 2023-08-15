import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Extra(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Extra')
        self.geometry('300x300')
        ttk.Label(self, text="Label").pack()
        ttk.Button(self, text="Button").pack()

def ask_yes_no():
    # ans = messagebox.askquestion('Title','body')
    # print(ans)
    messagebox.showerror("info", "error")


def create_window():
    global extra
    extra = Extra()
    # extra = tk.Toplevel()
    # extra.title("Extra")
    # extra.geometry("300x300")
    # ttk.Label(extra, text="Label").pack()
    # ttk.Button(extra, text="Button").pack()


def close_window():
    extra.destroy()


window = tk.Tk()
window.geometry('600x400')
window.title("Multiple Windows")

button1 = ttk.Button(window, text='open main window', command=create_window)
button1.pack(expand=True)

button2 = ttk.Button(window, text='close main window', command=close_window)
button2.pack(expand=True)

button3 = ttk.Button(
    window, text='create yes or no window', command=ask_yes_no)
button3.pack(expand=True)

window.mainloop()
