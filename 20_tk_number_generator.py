import tkinter as tk
from tkinter import messagebox
import random

def generate_numbers():
    try:
        start = int(start_entry.get())
        end = int(end_entry.get())
        count = int(count_entry.get())
        
        if start > end:
            messagebox.showerror("Error", "Start value must be less than or equal to end value.")
            return
        
        generated_numbers = random.sample(range(start, end + 1), count)
        result_text = ", ".join(str(num) for num in generated_numbers)
        result_label.configure(text=result_text)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid integer values.")

root = tk.Tk()
root.title("Number Generator")
root.geometry("300x200")

start_label = tk.Label(root, text="Start:")
start_label.pack()
start_entry = tk.Entry(root)
start_entry.pack()

end_label = tk.Label(root, text="End:")
end_label.pack()
end_entry = tk.Entry(root)
end_entry.pack()

count_label = tk.Label(root, text="Count:")
count_label.pack()
count_entry = tk.Entry(root)
count_entry.pack()

generate_button = tk.Button(root, text="Generate", command=generate_numbers)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
