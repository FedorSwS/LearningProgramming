# Таблица умножения
def multiplication_table(size):
    print("   |", end = "")
    for i in range(1, size + 1):
        print(f"{i:4}", end = "")
    print("\n" 
          + "---:" 
          + size * "----")
    
    for i in range(1, size + 1):
        print(f"{i:2} |", end = "")
        for j in range(1, size + 1):
            print(f"{i * j:4}", end = "")
        print()
multiplication_table(9)

# Факториал числа
def factorial (number):
    if number < 0:
        return "Факториал числа не определён."
    if number == 0 or number == 1:
        return 1
    return number * factorial (number - 1)
print(factorial(5))

# Список простых чисел до 100
import math
def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True
def list_prime_numbers():
    return [number for number in range (101) if is_prime_number(number)]
for x in list_prime_numbers():
    print(x, end = " ")
    
# Сортировка списка пузырьком
def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list [j + 1]:
                list[j], list[j + 1] = list [j + 1], list [j]
    return list
A = [2, 4, 7, 5, 5, 1, 10]
print()
print(bubble_sort(A))    
            
# Построение графика y = x**2
import matplotlib.pyplot as plt
def plot_function():
    x = [i for i in range(-10, 11)]
    y = [j**2 for j in x]
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title("График функции $y = x^2$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()
plot_function()