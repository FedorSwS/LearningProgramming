import tkinter as tk
from tkinter import messagebox

def say_hello():
    messagebox.showinfo("Привет!", "Привет, пользователь!")

root = tk.Tk()
root.title("ЛР №5")
root.geometry("400x200")
tk.Button(text="Привет", command=say_hello, font=("Times New Roman", 14)).pack(pady=50)
root.mainloop()