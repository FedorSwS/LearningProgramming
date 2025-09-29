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