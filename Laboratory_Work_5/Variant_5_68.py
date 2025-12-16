import tkinter as tk
from tkinter import ttk, messagebox

def calculate_sum():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        label_sum_result.config(text=f"{a + b}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа")

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_cur = combo_from.get()
        to_cur = combo_to.get()
        rates = {"RUB": 1.00, "USD": 78.92, "EUR": 91.37}
        if from_cur not in rates or to_cur not in rates:
            messagebox.showerror("Ошибка", "Выберите валюты из списка")
            return
        rub = amount * rates[from_cur]
        result = rub / rates[to_cur]
        label_result.config(text=f"{result:.2f} {to_cur}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число")

def exit_app():
    if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
        root.destroy()

def open_second_window():
    second = tk.Toplevel(root)
    second.title("Дополнительные функции")
    second.geometry("350x200")
    tk.Label(second, text="Изменить фон главного окна", font=("Times New Roman", 10)).pack(pady=(10, 5))
    color_var = tk.StringVar(value="white")
    color_combo = ttk.Combobox(
        second,
        textvariable=color_var,
        values=["white", "lightblue", "lightgreen", "lightyellow", "pink", "gray"],
        state="readonly",
        width=12
    )
    color_combo.pack(pady=5)
    def apply_color():
        root.configure(bg=color_var.get())
        style = ttk.Style()
        style.configure("TFrame", background=color_var.get())
    tk.Button(second, text="Применить цвет", command=apply_color, font=("Times New Roman", 10)).pack(pady=10)
    tk.Button(second, text="Закрыть", command=second.destroy, font=("Times New Roman", 10)).pack(pady=10)
    
root = tk.Tk()
root.title("ЛР №5")
root.geometry("420x320")
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=5, pady=5)

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

tab_calc = ttk.Frame(notebook)
notebook.add(tab_calc, text="Сумматор")
frame_sum = tk.Frame(tab_calc)
frame_sum.pack()
label_sum = tk.Label(frame_sum, text="Введите два числа для суммирования", font=("Times New Roman", 12)).pack(side="top", anchor="center", pady=10)
entry_a = tk.Entry(frame_sum, width=10)
entry_a.pack(side="left", padx=(15,5))
tk.Label(frame_sum, text="+").pack(side="left", padx=5)
entry_b = tk.Entry(frame_sum, width=10)
entry_b.pack(side="left", padx=(5,15))
tk.Button(frame_sum, text="=", command=calculate_sum).pack(side="left", padx=5)
label_sum_result = tk.Label(frame_sum, text="", font=("Times New Roman", 12))
label_sum_result.pack(side="left", padx=5)

tab_conv = ttk.Frame(notebook)
notebook.add(tab_conv, text="Конвертер")
tk.Label(tab_conv, text="Сумма:").pack(pady=(10, 2))
entry_amount = tk.Entry(tab_conv, width=15, font=("Times New Roman", 12))
entry_amount.pack()
frame_currency = tk.Frame(tab_conv)
frame_currency.pack(pady=10)
tk.Label(frame_currency, text="Из:").pack(side="left", padx=5)
combo_from = ttk.Combobox(frame_currency, values=["RUB", "USD", "EUR"], state="readonly", width=8)
combo_from.set("EUR")
combo_from.pack(side="left", padx=5)
tk.Label(frame_currency, text="В:").pack(side="left", padx=5)
combo_to = ttk.Combobox(frame_currency, values=["RUB", "USD", "EUR"], state="readonly", width=8)
combo_to.set("USD")
combo_to.pack(side="left", padx=5)
tk.Button(tab_conv, text="Конвертировать", command=convert_currency).pack(pady=10)
label_result = tk.Label(tab_conv, text="", font=("Times New Roman", 12), fg="green")
label_result.pack()

tab_extra = ttk.Frame(notebook)
notebook.add(tab_extra, text="Дополнительно")
tk.Button(tab_extra, text="Открыть второе окно", command=open_second_window).pack(pady=(10, 20), fill="both", expand=True)

root.mainloop()