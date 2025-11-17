def squares_of_numbers():
    return list(map(lambda x: x ** 2, range(1, 11)))
print("Квадраты чисел 1–10:", squares_of_numbers())

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib = fibonacci_generator()
print([next(fib) for i in range(20)])

def log_calls(func):
    def wrapper(*args):
        result = func(*args)
        print(f"Функция {func.__name__} вернула: {result}")
        return result
    return wrapper
@log_calls
def squares(numbers):
    return list(map(lambda x: x ** 2, numbers))
squares([1,2,4,6,8,10])

def round_list_result(digits = 2):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            return [f"{x:.{digits}f}" for x in result]
        return wrapper
    return decorator
@round_list_result(digits = 3)
def list_for_round():
    return [3.159, 2.7128, 1.41, 0.577212]
print(list_for_round())

import csv

def read_and_process_csv(filename):
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    headers = rows[0]
    data_rows = rows[1:]
    return headers, data_rows
headers, data_rows = read_and_process_csv('C:/Users/SoNiC/Desktop/LearningProgramming/Laboratory_Work_4/lr4.csv')
high_achievers = list(map(
    lambda row: dict(zip(headers, row)),
    filter(lambda row: float(row[1]) >= 4.0, data_rows)
))
third_course = list(map(
    lambda row: dict(zip(headers, row)),
    filter(lambda row: row[2] == '3', data_rows)
))
print("     Студенты с оценкой >= 4.0:")
for s in high_achievers:
    print(s)
print("\n     Студенты на 3 курсе:")
for s in third_course:
    print(s)