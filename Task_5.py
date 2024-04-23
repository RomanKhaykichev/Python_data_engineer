"""Урок 5. Итераторы и генераторы"""

"""1. Решить задачи, которые не успели решить на семинаре."""

"""2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""

# Ver_1

import os # pathlib

def parse_file_path(link: str) -> tuple:
    """Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
    
    : Используя модуль 'os'
    """
    path, file_name = os.path.split(link)
    name, extension = os.path.splitext(file_name)
    return path, name, extension

# Ver_2

def path_unpacking_elements(link: str) -> tuple:
    '''Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.'''
    *_, file_name_extension  = link.split('/')
    name, extension = file_name_extension.split('.')
    path = link[:-len(file_name_extension)]
    return path, name, extension


if __name__ == '__main__':
    path_to_file = 'https://docs.python.org/3/library/pathlib.html'
    print(f'Ver_1 - {parse_file_path(path_to_file)}')
    print(f'Ver_2 - {path_unpacking_elements(path_to_file)}')


"""3. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии"""

name_list = ['Viktor', 'Andrew', 'Ivan']
rate_list = [20_000, 15_000, 30_000]
percent_list = ['10.55%', '15.70%', '30.25%']

print({name: rate * float(percent[:-1]) for name, rate, percent in zip(name_list, rate_list, percent_list)})


"""4. Создайте функцию генератор чисел Фибоначчи https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8"""

def generate_fibonacci(number: int):
    """генератор чисел Фибоначчи"""
    a, b = 0, 1
    yield a
    yield b
    for _ in range(number - 2):
        yield a + b
        a, b = b, a + b


print(*generate_fibonacci(11))

