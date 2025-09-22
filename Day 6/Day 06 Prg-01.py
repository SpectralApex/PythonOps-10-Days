# Traffic Light Simulation using Tkinter
import tkinter as tk

window = tk.Tk()
window.title("Traffic Light Simulation")
window.geometry("200x400")
window.configure(bg="black")

canvas = tk.Canvas(window, width=150, height=350, bg="black")
canvas.pack(pady=20)

red_light = canvas.create_oval(30, 30, 120, 120, fill="gray")
yellow_light = canvas.create_oval(30, 130, 120, 220, fill="gray")
green_light = canvas.create_oval(30, 230, 120, 320, fill="gray")

def change_light():
    current = canvas.itemcget(red_light, "fill")
    if current == "red":
        canvas.itemconfig(red_light, fill="gray")
        canvas.itemconfig(yellow_light, fill="yellow")
        window.after(1000, change_light)
    elif canvas.itemcget(yellow_light, "fill") == "yellow":
        canvas.itemconfig(yellow_light, fill="gray")
        canvas.itemconfig(green_light, fill="green")
        window.after(3000, change_light)
    elif canvas.itemcget(green_light, "fill") == "green":
        canvas.itemconfig(green_light, fill="gray")
        canvas.itemconfig(red_light, fill="red")
        window.after(3000, change_light)

canvas.itemconfig(red_light, fill="red")
window.after(3000, change_light)

window.mainloop()
