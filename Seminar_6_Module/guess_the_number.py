"""Task_2
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""

from random import randint


def guess_number(lower_limit=0, upper_limit=100, count=10):
    """Если число угадано, возвращается истина, а если попытки исчерпаны - ложь
    
    :Функция выводит подсказки “больше” и “меньше”.
    """
    number_to_guess = randint(lower_limit, upper_limit)
    i = 0 
    while i < count:
        number = int(input(f'Попытка {i+1}/{count} Введите число: '))
        if number == number_to_guess:
            print('You are a winner!')
            break
        if number > number_to_guess:
            print('The number is less!')
        else:
            print('The number is greater!')
        i += 1
    else:
        print('You lose...')

if __name__ == '__main__':
    lower_limit = int(input('Lower limit: '))
    upper_limit = int(input('Upper limit: '))
    count = int(input('Count: '))
    guess_number(lower_limit, upper_limit, count)