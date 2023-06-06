import tkinter as tk
from tkinter import ttk
from random import choice
window = tk.Tk()
window.title("TreeView")
window.geometry('600x400')

# Data
first_name = ["Mohit","Bob","Alex","James"]
last_name = ["Mehra","Smith","Wilson","Gunn"]

# TreeView
table = ttk.Treeview(window,columns = ('first','last','email'),show = 'headings')
table.heading('first',text="First Name")
table.heading('last',text="Last Name")
table.heading('email',text="Emial")
table.pack(fill= 'both',expand=True)

# Insert Value
# table.insert(parent = '',index = 0,values = ("Mohit","Mehra","Mohit@gmial.com"))
for i in range(100):
    first = choice(first_name)
    last = choice(last_name)
    emial = f'{first}{last}@gmail.com'
    data = (first,last,emial)
    table.insert(parent = '',index = 0, values = data)

table.insert(parent = '',index = tk.END, values = ('XXXX','YYYY','ZZZZ'))

# Event
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])
    # table.item(table.selection())
def delete_item(_):
    print("Delete")
    for i in table.selection():
        table.delete(i)
        
table.bind("<<TreeviewSelect>>",item_select)
table.bind("<Delete>",delete_item)
window.mainloop()