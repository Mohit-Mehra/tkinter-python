import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x600")
window.title("Combined Layout")
window.minsize(600, 600)

# Main Layout Widgets
menu_frame = ttk.Frame(window)
main_frame = ttk.Frame(window)

# main Place Layout
menu_frame.place(x=0, y=0, relwidth=0.3, relheight=1)
main_frame.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

# Menu Widgets
menu_button1 = ttk.Button(menu_frame, text="Button 1")
menu_button2 = ttk.Button(menu_frame, text="Button 2")
menu_button3 = ttk.Button(menu_frame, text="Button 3")

menu_Slider1 = ttk.Scale(menu_frame, orient='vertical')
menu_Slider2 = ttk.Scale(menu_frame, orient='vertical')

toggle_frame = ttk.Frame(menu_frame)
menu_toggle1 = ttk.Checkbutton(toggle_frame, text='Check 1')
menu_toggle2 = ttk.Checkbutton(toggle_frame, text='Check 2')

entry = ttk.Entry(menu_frame)

# Menu Layout
menu_frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
menu_frame.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

menu_button1.grid(row=0, column=0, sticky='news', columnspan=2)
menu_button2.grid(row=0, column=2, sticky='news')
menu_button3.grid(row=1, column=0, sticky='news', columnspan=3)

menu_Slider1.grid(row=2, column=0, rowspan=2, sticky="news", pady=20)
menu_Slider2.grid(row=2, column=2, rowspan=2, sticky="news", pady=20)

# Toggle Layout
toggle_frame.grid(row=4, column=0, columnspan=3, sticky="news")
menu_toggle1.pack(side='left', expand=True)
menu_toggle2.pack(side='left', expand=True)

# Entry Layout
entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor='center')

# Main Widgets
entry_frame1 = ttk.Frame(main_frame)
main_label1 = ttk.Label(entry_frame1, text='label 1', background='cyan')
main_button1 = ttk.Button(entry_frame1, text="Button 1")

entry_frame2 = ttk.Frame(main_frame)
main_label2 = ttk.Label(entry_frame2, text='label 2', background='skyblue')
main_button2 = ttk.Button(entry_frame2, text="Button 2")

# Main Layout
entry_frame1.pack(side="left", expand=True, fill='both', padx=20, pady=20)
entry_frame2.pack(side="left", expand=True, fill='both', padx=20, pady=20)

main_label1.pack(expand=True, fill='both')
main_button1.pack(expand=True, fill='both', pady=10)

main_label2.pack(expand=True, fill='both')
main_button2.pack(expand=True, fill='both', pady=10)

window.mainloop()
