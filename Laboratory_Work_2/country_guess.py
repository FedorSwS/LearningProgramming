import random
countries = [
    "Россия", "США", "Китай", "Германия", "Франция", 
    "Италия", "Япония", "Канада", "Бразилия", "Индия",
    "Австралия", "Мексика", "Испания", "Украина", "Турция",
    "Египет", "Польша", "Аргентина", "Швеция", "Норвегия"
]
def hint(country):
    if len(country) > 4:
        return f"Подсказка: в названии {len(country)} букв"
    else:
        return "Подсказка: в названии страны мало букв"
def play():
    country = random.choice(countries)
    first_letter = country[0]
    attempts = 3
    hint_used = False
    print(f"Угадай страну! Первая буква: '{first_letter}'")
    print(f"У тебя {attempts} попытки")
    for attempt in range(attempts):
        guess = input(f"\nПопытка {attempt + 1}: ").strip()
        if guess.lower() == country.lower():
            print(f"Правильно! Это {country}!")
            return True
        else:
            if attempt == 0 or attempt == 1 and not hint_used:
                use_hint = input("Неправильно! Хочешь подсказку? (да/нет): ").strip().lower()
                if use_hint in ['да', 'д', 'yes', 'y']:
                    print(hint(country))
                    hint_used = True
                else:
                    print("Продолжаем угадывать!")
            elif attempt < attempts - 1:
                print("Неправильно, попробуй еще!")
            else:
                print(f"Попытки закончились! Это была {country}")
    return False
def show_countries():
    print("Страны для угадывания:")
    for i in range(len(countries)):
        print(f"{i+1}. {countries[i]}")