"""Task_4
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
"""

def secrets(puzzle: str, answers: list[str], count=3) -> int:
    """Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
    
    :Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
    """
    print(f'Угадай загадку.\n{puzzle}')
    for i in range(1, count+1):
        ans = input(f'Попытка номер {i}: ').lower()
        if ans in answers:
            return i
    return 0


# if __name__ == '__main__':
#     result = secrets('Зимой и летом одним цветом', ['ель', 'ёлка', 'сосна'])
#     print(f'Угадал с {result} попытки' if result > 0 else 'Не угадал')

"""Task_5
Добавьте в модуль с загадками функцию, которая хранит словарь списков. Ключ словаря - загадка,
значение - список с отгадками. Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
"""

def storage():
    """Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
    
    :Ключ словаря - загадка
    :Значение - список с отгадками.
    """
    puzzles = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
        'Не лает, не кусает, в дом не пускает': ['замок'],
        'Сидит дед во сто шуб одет': ['лук', 'луковица'],
    }
    for key, value in puzzles.items():
        result = secrets(key, value)
        print(f'Угадал с {result} попытки' if result > 0 else 'Не угадал')


# if __name__ == '__main__':
#     storage()

"""Task_6
Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания. Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря
в удобном для чтения виде. Для формирования результатов используйте генераторное выражение.
"""

_data = {}


def storage_with_generator_result():
    """функция выводит результаты угадывания из защищённого словаря.
    
    :Ключ словаря - загадка
    :Значение - список с отгадками.
    """
    puzzles = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
        'Не лает, не кусает, в дом не пускает': ['замок'],
        'Сидит дед во сто шуб одет': ['лук', 'луковица'],
    }
    for key, value in puzzles.items():
        result = secrets(key, value)
        print(f'Угадал с {result} попытки' if result > 0 else 'Не угадал')
        yield key, result


def save(puzzle: str, count: int):
    """Сохраняет результаты угадывания в защищенный словарь"""
    _data.update({puzzle: count})


def show():
    """Выводит результаты угадывания из защищенного словаря"""
    res = (f'Загадку "{key}" разгадали с {value}-й попытки' if value > 0
           else f'Загадку "{key}" не разгадали'
           for key, value in _data.items())
    print('\n'.join(res))


if __name__ == '__main__':
    generator = storage_with_generator_result()
    for key, result in generator:
        save(key, result)
    show()