import tkinter as tk
from tkinter import ttk, messagebox

def say_hello():
    messagebox.showinfo("Привет!", "Привет, пользователь!")

def calculate_sum():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        result = a + b
        label_sum_result.config(text=f"{result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа")

def exit_app():
    if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
        root.destroy()
        
root = tk.Tk()
root.title("ЛР №5")
root.geometry("400x200")
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

tab_hello = ttk.Frame(notebook)
notebook.add(tab_hello, text="Приветствие")
tk.Button(tab_hello, text="Привет", command=say_hello, font=("Times New Roman", 14)).pack(pady=50)

tab_calculator = ttk.Frame(notebook)
notebook.add(tab_calculator, text="Сумматор")
entry_a = tk.Entry(tab_calculator, width=10)
entry_a.pack(side="left", padx=15)
tk.Label(tab_calculator, text="+").pack(side="left")
entry_b = tk.Entry(tab_calculator, width=10)
entry_b.pack(side="left", padx=15)
tk.Button(tab_calculator, text="=", command=lambda: calculate_sum()).pack(side="left", padx=15)
label_sum_result = tk.Label(tab_calculator, text="", font=("Arial", 12))
label_sum_result.pack(side="left", padx=5)

root.mainloop()