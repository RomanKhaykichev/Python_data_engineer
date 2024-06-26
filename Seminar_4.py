"""Урок 4. Функции"""

"""
Косая черта / и звёздочка * разделяют позиционные и ключевые параметры
def func(positional_only, /, positional_or_keyword, *, keyword_only):
    pass
 
Параметры *args и **kwargs
Имена args и kwargs — общепринятое соглашение
✔ def func(*args): — принимает любое число позиционных аргументов -> # кортеж
✔ def func(**kwargs): — принимает любое число ключевых аргументов -> # словарь
✔ def func(*args, **kwargs): — принимает любое число позиционных и ключевых аргументов
 

sorted(my_dict.items(), key=lambda x: x[1])


def func(*args):
'''function instruction

:ssdsdsd
:dsdsdsd
'''
m = gloat('-inf)
for item in args:
    if m < < 100:
        m = item
returm m

map(), filter(), zip()

map(function, iterable)
Принимает на вход функцию и последовательность. Функция применяется к каждому элементу последовательности и возвращает map итератор.
filter(function, iterable)
Принимает на вход функцию и последовательность. Если функция возвращает истину, элемент остаётся в последовательности. Как и map возвращает объект итератор.
zip(*iterables, strict=False)
Принимает несколько последовательностей и итерируется по ним параллельно. Если передать ключевой аргумент 
strict=True, вызовет ошибку ValueError в случае разного числа элементов в каждой из последовательностей.

max(lst, default='empty')
min(lst_turples, key=lambda x: x[1])
sum(num, start=number)

Функции all(), any()
✔ all(iterable) Функция возвращает истину, если все элементы последовательности являются истиной.
✔ any(iterable) Функция возвращает истину, если хотя бы один элемент последовательности являются истиной.

✔ chr(integer)Функция возвращает строковой символ из таблицы Юникод по его номеру. Номер — целое число от 0 до 1_114_111.
✔ ord(char)Функция принимает один символ и возвращает его код в таблице Юникод

✔ locals() Функция возвращает словарь переменных из локальной области видимости на момент вызова функции.
✔ globals() Функция возвращает словарь переменных из глобальной области видимости, т.е. из пространства модуля. 
✔ vars() Функция без аргументов работает аналогично функции locals(). Если передать в vars объект,
функция возвращает его атрибут __dict__. А если такого атрибута нет у объекта, вызывает ошибку TypeError.

 """

"""Task_1
Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
Строки нумеруются начиная с единицы.
Слова выводятся отсортированными согласно кодировки Unicode.
Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
"""

def print_text(text: str):
    """Функция принемает строку текста и возвращает каждое слово с новой строки"""
    text_lst = text.split(' ')
    text_lst.sort()

    max_len = max([len(word) for word in text_lst])
    max_len_2 = len(max(text_lst, key=len))

    for i, word in enumerate(text_lst, 1):
        print(f'{i}  {word: >{max_len}}')


if __name__ == '__main__':
    print_text(input('input text: '))

"""Task_2
Напишите функцию, которая принимает строку текста.
Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""

def text_unicode(text: str) -> list:
    """формируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.
    
    Сформируйте список с уникальными кодами Unicode каждого
    символа введённой строки отсортированный по убыванию.
    """
    return list(map(ord, sorted(set(text), reverse=True)))


if __name__ == '__main__':
    print(text_unicode(input('Write text: ')))


"""Task_3
Функция получает на вход строку из двух чисел через пробел.
Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.
"""

def unicode_range(text: str) -> dict:
    """Возвращает словарь символов"""
    a, b = [int(i) for i in text.split()]
    return {chr(i):i for i in range(a, b+1)}


if __name__ == '__main__':
    print(unicode_range(input('Two numbers: ')))

"""Task_4
Функция получает на вход список чисел.
Отсортируйте его элементы in place без использования встроенных в язык сортировок.
Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""

def sort_numbers(num_list: list) -> None:
    """sort number in place"""
    for _ in range(len(num_list)):
        for j in range(len(num_list) - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]


if __name__ == '__main__':
    lst = [int(i) for i in input('Numbers: ').split()]
    sort_numbers(lst)
    print(lst)

"""Task_5
Функция принимает на вход три списка одинаковой длины:
имена str,
ставка int,
премия str с указанием процентов вида «10.25%».
Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии.
"""

def calculate_bonus(names: list[str], rate: list[int], percents: list[str]) -> dict:
    """Рассчет премии."""
    dict_bonus = {}
    for names, rate, percents in zip(names, rate, percents):
        dict_bonus[names] = rate * float(percents[:-1]) / 100
        # dict_bonus.setdefault(names, rate * float(percents.replace('%', '')))
    return dict_bonus


if __name__ == '__main__':
    names = ['Alex', 'Andrew', 'Anton']
    rate = [30_000, 35_000, 50_000]
    percents = ['10.5%', '12.5%', '14.9%']
    print(calculate_bonus(names, rate, percents))

"""Task_6
Функция получает на вход список чисел и два индекса.
Вернуть сумму чисел между переданными индексами.
Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""

def sum_range(numbers: list, x_1: int, x_2: int) -> int:
    """Вернуть сумму чисел между переданными индексами"""
    if x_1 > x_2:
        x_1, x_2 = x_2, x_1
    if x_1 < 0:
        x_1 = 0
    if x_2 >= len(numbers):
        x_2 = len(numbers) - 1
    return sum(numbers[x_1:x_2+1])


if __name__ == '__main__':
    numbers = [4, 45, 32, 434, 3, 32, 30, 5]
    x_1 = 5
    x_2 = 3
    print(sum_range(numbers, x_1, x_2))

"""Task_7
Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, верните истину,
а если хотя бы одна убыточная — ложь.
"""

COMPANY_PROFIT = 19


def calculate_result(company_dictionary: dict) -> bool:
    """Возвращает истину, если все компании прибыльные """
    lst = [sum(value) > COMPANY_PROFIT for value in company_dictionary.values()]
    print(lst)
    return all(lst)
    

if __name__ == '__main__':
    company_dictionary = {
    'Micr': [2, 3, 4, 5, 6],
    'JMT': [3, 2, 5 , 6, 5],
    'PLS': [4, 2, 5, 5, 7],
}
    print(calculate_result(company_dictionary))

"""Task_8
Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None.
Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""

# variables = ['room', 'cupcakes', 'coffee', 'cakes', 'sales']

# def change_end_s(lst: list) -> list:
#     """return without 's'"""
#     lst_with_s = []
#     for word in lst:
#         for letters in range(len(word)):
#             if word[letters] == 's':
#                 lst_with_s.append(word)
#                 lst.pop(lst.index(word))

#     return lst_with_s


def no_s():
    """delete from list variables end with 's'"""
    lst = {}
    for var, value in globals().items():
        if var != "s" and var.endswith("s") and var != "no_s":
            lst[var[:-1]] = value
            globals()[var] = None
    for k, v in lst.items():
        globals()[k] = v


if __name__ == '__main__':
    items = 0
    names = 'dsdsd'
    s = 5
    value = 'ftft'
    print(globals())
    no_s()
    print(globals())
