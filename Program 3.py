import tkinter as tk
from tkinter import messagebox

def calculate_charge():
    try:
        minutes = float(entry_minutes.get())
        if rate.get() == 1:
            cost = minutes * 0.02
        elif rate.get() == 2:
            cost = minutes * 0.12
        else:
            cost = minutes * 0.05
        messagebox.showinfo("Call Charge", "Charge: $" + str(round(cost, 2)))
    except:
        messagebox.showerror("Error", "Enter valid number of minutes")

root = tk.Tk()
root.title("Long Distance Charges")
root.geometry("350x300")

rate = tk.IntVar()
rate.set(1)

tk.Label(root, text="Select Rate Category").pack(pady=10)

tk.Radiobutton(root, text="Daytime ($0.02/min)", variable= rate, value= 1).pack(anchor= "w")
tk.Radiobutton(root, text="Evening ($0.12/min)", variable= rate, value= 2).pack(anchor= "w")
tk.Radiobutton(root, text="Off-Peak ($0.05/min)", variable= rate, value= 3).pack(anchor= "w")

tk.Label(root, text="Enter Minutes").pack(pady=10)
entry_minutes = tk.Entry(root)
entry_minutes.pack()

tk.Button(root, text="Calculate Charge", command=calculate_charge).pack(pady=15)

root.mainloop()
