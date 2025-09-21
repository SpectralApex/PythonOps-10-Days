# digital_clock.py
# Tkinter digital clock
import tkinter as tk
import time

def update():
    current = time.strftime("%H:%M:%S")
    label.config(text=current)
    root.after(200, update)

root = tk.Tk()
root.title("Digital Clock")
label = tk.Label(root, font=("Helvetica", 72), bg="black", fg="lime")
label.pack(padx=20, pady=20)
update()
root.mainloop()
