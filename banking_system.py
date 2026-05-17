import tkinter as tk
from tkinter import messagebox

balance = 0

def deposit():
    global balance
    amount = float(entry.get())
    balance += amount
    result.config(text=f"Balance: ₹{balance}")

def withdraw():
    global balance
    amount = float(entry.get())

    if amount > balance:
        messagebox.showerror("Error", "Insufficient Balance")
    else:
        balance -= amount
        result.config(text=f"Balance: ₹{balance}")

root = tk.Tk()

root.title("Online Banking System")
root.geometry("400x300")

tk.Label(root, text="Enter Amount").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Deposit", command=deposit).pack(pady=10)

tk.Button(root, text="Withdraw", command=withdraw).pack(pady=10)

result = tk.Label(root, text="Balance: ₹0")
result.pack(pady=20)

root.mainloop()
