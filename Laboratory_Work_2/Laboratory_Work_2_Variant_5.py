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
print()

# # Подсчёт гласных
# list_vowels = ['а', 'о', 'у', 'э', 'ы', 'я', 'ю', 'е', 'ё', 'и']
# counter = 0
# string = str(input())
# for i in range (len (string)):
#     if string[i] in list_vowels:
#         counter += 1
# print(counter)

# Таблица умножения
def multiplication_table(size):
    print("   |", end = "")
    for i in range(1, size + 1):
        print(f"{i:4}",end = "")
    print("\n"
          + "---+"
          + size * "----")
    for i in range(1, size + 1):
        print(f"{i:2} |", end = "")
        for j in range(1, size + 1):
            print(f"{i*j:4}", end = "")
        print()
multiplication_table(20)

# Бинарный поиск
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    mid = 0
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            return mid
    return -1

arr = [ 0, 1, 3, 3, 12 ]
x = 13
result = binary_search(arr, x)
if result != -1:
    print(f"Элемент {x} найден с индексом:", str(result))
else:
    print(f"Элемент {x} не найден")