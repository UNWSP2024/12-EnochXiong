import tkinter
from tkinter import messagebox

def calc_mileage():
    try:
        mileage = float(miles.get()) / float(gallons.get())
        messagebox.showinfo("Result", "MPG: " + str(round(mileage, 2)))
    except:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tkinter.Tk()
root.title("MPG Calculator")
root.geometry("400x300")

tkinter.Label(root, text="Gallons").pack(pady=10)
gallons = tkinter.Entry(root)
gallons.pack(pady=5)

tkinter.Label(root, text="Miles").pack(pady=10)
miles = tkinter.Entry(root)
miles.pack(pady=5)

tkinter.Button(root, text="Calculate MPG", command=calc_mileage).pack(pady=15)

root.mainloop()
