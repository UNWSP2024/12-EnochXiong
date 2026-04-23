import tkinter as tk
from tkinter import messagebox

def calculate_total():
    total = 0

    if oil.get():
        total += 30
    if lube.get():
        total += 20
    if flush.get():
        total += 40
    if trans.get():
        total += 100
    if inspect.get():
        total += 35
    if muffler.get():
        total += 200
    if tire.get():
        total += 20
    messagebox.showinfo("Total Charges", "Total: $" + str(total))

root = tk.Tk()
root.title("Joe's Automotive")
root.geometry("350x400")

oil = tk.IntVar()
lube = tk.IntVar()
flush = tk.IntVar()
trans = tk.IntVar()
inspect = tk.IntVar()
muffler = tk.IntVar()
tire = tk.IntVar()

tk.Label(root, text="Select Services", font=("Arial", 14)).pack(pady=10)
tk.Checkbutton(root, text="Oil Change ($30)", variable=oil).pack(anchor="w")
tk.Checkbutton(root, text="Lube Job ($20)", variable=lube).pack(anchor="w")
tk.Checkbutton(root, text="Radiator Flush ($40)", variable=flush).pack(anchor="w")
tk.Checkbutton(root, text="Transmission Fluid ($100)", variable=trans).pack(anchor="w")
tk.Checkbutton(root, text="Inspection ($35)", variable=inspect).pack(anchor="w")
tk.Checkbutton(root, text="Muffler Replacement ($200)", variable=muffler).pack(anchor="w")
tk.Checkbutton(root, text="Tire Rotation ($20)", variable=tire).pack(anchor="w")
tk.Button(root, text="Calculate Total", command=calculate_total).pack(pady=15)

root.mainloop()
