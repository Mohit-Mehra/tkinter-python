import tkinter as tk
from tkinter import messagebox
import time


class PomodoroApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro App")

        self.timer_label = tk.Label(self, text="25:00", font=("Helvetica", 36))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(self, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.close_button = tk.Button(self, text="Close", command=self.close_app)
        self.close_button.pack(pady=10)

        self.timer_running = False
        self.time_remaining = 1500  # 25 minutes in seconds

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.run_timer()

    def run_timer(self):
        if self.timer_running:
            minutes = self.time_remaining // 60
            seconds = self.time_remaining % 60
            timer_text = f"{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=timer_text)

            if self.time_remaining > 0:
                self.time_remaining -= 1
                self.after(1000, self.run_timer)
            else:
                self.timer_running = False
                messagebox.showinfo("Pomodoro Timer", "Time's up!")

    def close_app(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()


if __name__ == "__main__":
    app = PomodoroApp()
    app.mainloop()
