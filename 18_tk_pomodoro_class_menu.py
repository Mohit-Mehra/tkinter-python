import tkinter as tk
from tkinter import messagebox
import time


class PomodoroApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro App")

        self.timer_running = False
        self.time_remaining = 0

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Start", command=self.start_timer)
        file_menu.add_separator()
        file_menu.add_command(label="Close", command=self.close_app)

        menu_bar.add_cascade(label="File", menu=file_menu)

    def create_widgets(self):
        self.timer_label = tk.Label(self, text="00:00", font=("Arial", 48))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(self, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.close_button = tk.Button(self, text="Close", command=self.close_app)
        self.close_button.pack(pady=10)

    def start_timer(self):
        if not self.timer_running:
            self.time_remaining = 25 * 60  # 25 minutes
            self.update_timer()
            self.timer_running = True

    def update_timer(self):
        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        time_str = f"{minutes:02d}:{seconds:02d}"
        self.timer_label.configure(text=time_str)

        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.after(1000, self.update_timer)
        else:
            self.timer_running = False
            messagebox.showinfo("Pomodoro Timer", "Time's up!")

    def close_app(self):
        if self.timer_running:
            messagebox.showinfo("Pomodoro Timer", "Please stop the timer first.")
        else:
            self.destroy()


app = PomodoroApp()
app.mainloop()
