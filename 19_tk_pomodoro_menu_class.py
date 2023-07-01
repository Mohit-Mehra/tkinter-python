import tkinter as tk
from tkinter import messagebox
import time

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        self.master.geometry("300x200")
        
        self.is_running = False
        self.remaining_time = 1500  # 25 minutes in seconds (25 * 60)
        
        self.create_menu()
        self.create_timer_label()
        
    def create_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Start", command=self.start_timer)
        file_menu.add_command(label="Stop", command=self.stop_timer)
        file_menu.add_separator()
        file_menu.add_command(label="Close", command=self.master.quit)
        
    def create_timer_label(self):
        self.timer_label = tk.Label(
            self.master, text="", font=("Helvetica", 24), fg="blue"
        )
        self.timer_label.pack(pady=20)
        self.update_timer_label()
        
    def update_timer_label(self):
        minutes, seconds = divmod(self.remaining_time, 60)
        self.timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")
        if self.is_running:
            self.remaining_time -= 1
            if self.remaining_time < 0:
                self.stop_timer()
                self.show_notification("Time's up! Take a break.")
                self.remaining_time = 1500  # Reset to 25 minutes for the next round
        self.master.after(1000, self.update_timer_label)
        
    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.update_timer_label()
            
    def stop_timer(self):
        self.is_running = False

    def show_notification(self, message):
        messagebox.showinfo("Pomodoro Timer", message)


if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
