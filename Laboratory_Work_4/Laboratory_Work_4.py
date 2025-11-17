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