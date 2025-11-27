import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x150")
root.resizable(False, False)
root.config(bg="#111827")

title_label = tk.Label(
    root,
    text="Digital Clock",
    font=("Arial", 14, "bold"),
    bg="#111827",
    fg="#9CA3AF"
)
title_label.pack(pady=5)

time_label = tk.Label(
    root,
    text="00:00:00",
    font=("Arial", 32, "bold"),
    bg="#111827",
    fg="#FBBF24"
)
time_label.pack(pady=10)

update_time()
root.mainloop()
