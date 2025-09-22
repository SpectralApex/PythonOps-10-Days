# Spectral Scientific Calculator using Tkinter
import tkinter as tk
import math

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "√":
        try:
            result = math.sqrt(float(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

window = tk.Tk()
window.title("Spectral Scientific Calculator")
window.geometry("400x550")
window.resizable(False, False)

entry = tk.Entry(window, font="Arial 20", bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

btn_texts = [
    ["7", "8", "9", "/", "√"],
    ["4", "5", "6", "*", "("],
    ["1", "2", "3", "-", ")"],
    ["0", ".", "C", "+", "="]
]

for row in btn_texts:
    frame = tk.Frame(window)
    frame.pack(expand=True, fill="both")
    for btn in row:
        button = tk.Button(frame, text=btn, font="Arial 18", relief=tk.GROOVE)
        button.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        button.bind("<Button-1>", click)

window.mainloop()
