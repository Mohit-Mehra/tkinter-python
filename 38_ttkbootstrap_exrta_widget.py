import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter

# window
window = ttk.Window(themename='darkly')
window.title('Extra Widgets')

# Scrollable Frame
scroll_frame = ScrolledFrame(window)
scroll_frame.pack(expand=True, fill='both')

for i in range(100):
    frame = ttk.Frame(scroll_frame)
    ttk.Label(frame, text=f"Label : {i}").pack(fill='x', side='left')
    ttk.Button(frame, text=f"Button : {i}").pack(fill='x', side='left')
    frame.pack(fill='x', expand=True)

# Toast
toast = ToastNotification(
    title='This is a message title',
    message="Actual Message",
    duration=2000,
    bootstyle='dark',
    position=(0, 0, 'ne')
)
ttk.Button(window, text="Show Toast", command=toast.show_toast).pack()

# Tooltip
button = ttk.Button(window, text="Tooltip", bootstyle="warning")
button.pack(pady=10)
ToolTip(button, text="This is Tooltip", bootstyle="danger-inverse")

# calender
calender = DateEntry(window)
calender.pack(pady=10)

ttk.Button(window, text='get Calnder date',
           command=lambda: print(calender.entry.get())).pack()

# Progrss => Floodgauge
progress_int = tk.IntVar(value=50)
progress = ttk.Floodgauge(
    window,
    text='progress',
    variable=progress_int,
    bootstyle='danger',
    mask='mask {}%'
)
progress.pack(pady=10, fill='x')
ttk.Scale(window, from_=0, to=100, variable=progress_int).pack()

# Meter
meter = ttk.Meter(
    window,
    amounttotal=100,
    amountused=10,
    interactive=True,
    metertype='semi',
    subtext='other text',
    bootstyle='danger'
)
meter.pack()

window.mainloop()
