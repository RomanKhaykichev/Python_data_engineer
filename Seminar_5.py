"""Урок 5. Интераторы и генераторы"""


"""
- Однострочники -
 a, b = b, a
Обычная распаковка a, b, c = последовательность

Распаковка с упаковкой a, *b, c = последовательность

Распаковка со звёздочкой * последовательность

- Итераторы -
Функция iter()
✔ iter(object[, sentinel])
Функция принимает на вход object поддерживающий 
итерацию. Второй параметр функции iter — sentinel 
передают для вызываемых объектов-итераторов

Функция next()
✔ next(iterator[, default])
На вход функция принимает итератор, 
который вернула функция iter.
Второй параметр функции next — default 
нужен для возврата значения по умолчанию 
вместо выброса исключения StopIteration.

- Генераторы -

List comprehensions
✔ list_comp = [expression for expr in sequense1 if condition1 ...]
Генератор списков формирует list заполненный данным и присваивает его переменной.

Генераторные выражения или генерация списка
На выходе нужен готовый список?
✔ list comprehensions
✔ [квадратные скобки]
Элементы нужны последовательно?
✔ генераторное выражение
✔ (круглые скобки)

Set и dict comprehensions
Set comprehensions
set_comp = {expression for expr in sequense1 if condition1 …}
Dict comprehensions
dict_comp = {key: value for expr in sequense1 if condition1 …}
Сходства и различия
{используются фигурные скобки для выражения}
словарь подставляет ключ и значение через двоеточие

Создание функции генератора
Команда yield
Команда yield работает аналогично return.
Но вместо завершения функции запоминает её состояние. 
Повторный вызов продолжает код после yield.
def gen(*args, **kwargs):
 ...
 yield result

"""

"""Task_1
Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.

Сформируйте словарь, где:
второе и третье число являются ключами.
первое число является значением для первого ключа.
четвертое и все возможные последующие числа
хранятся в кортеже как значения второго ключа.
"""

a, b, c, *d = input('четырё или более целых чисел, разделённых символом “/”: ').split('/')
dictionary = {b: a, c: tuple(d)}
print(dictionary)

"""Task_2
Самостоятельно сохраните в переменной строку текста.
Создайте из строки словарь, где ключ — буква, а значение — код буквы.
Напишите преобразование в одну строку.
"""

text = 'Без труда не выловить и рыбку из пруда!'
print({key: ord(key) for key in text}) # dict comprehension

"""Task_3
Продолжаем развивать задачу 2.
Возьмите словарь, который вы получили.
Сохраните его итератор.
Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
"""
import sys

text = 'Без труда не выловить и рыбку из пруда!'
dictionary_char = {key: ord(key) for key in text}
iter_dictionary = iter(dictionary_char.items())
# print(iter_dictionary, type(iter_dictionary), sys.getsizeof(iter_dictionary), sys.getsizeof(dictionary_char))
# print(next(iter_dictionary)) - забирает и забывает из словаря.
for item in range(5):
    print(next(iter_dictionary))

"""Task_4
Создайте генератор чётных чисел от нуля до 100.
Из последовательности исключите числа, сумма цифр которых равна 8.
Решение в одну строку.
"""

# Ver_1
print(*(i for i in range(0, 101, 2) if sum(map(int, str(i))) != 8))

# Ver_2
print(*(i for i in range(0, 101, 2) if sum([int(j) for j in str(i)]) != 8))

"""Task_5
Напишите программу, которая выводит на экран числа от 1 до 100.
При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
Вместо чисел, кратных пяти — слово «Buzz».
Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
*Превратите решение в генераторное выражение.
"""

print(*('FizzBuzz' if i % 3 == 0 and i % 5 == 0
        else 'Fizz' if i % 3 == 0
        else 'Buzz' if i % 5 == 0
        else i
        for i in range(1, 101)))

"""Task_6
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.
Для вывода результата используйте «принт» без перехода на новую строку.
"""

print(*(f'{i} * {j} = {i * j} \t \t' if i < 6 else ('\n')
      for j in range(2, 11) for i in range(2, 7)))

print(*(f'{i} * {j} = {i * j} \t \t' if i < 10 else ('\n')
      for j in range(2, 11) for i in range(6, 11)))

"""Task_7
Создайте функцию-генератор.
Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте правило: «число является простым, если делится нацело только на единицу и на себя».
"""

def prime(n):
    if n < 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_simple():
    n = 2
    while True:
        if prime(n):
            yield n
        n += 1


j = generate_simple()
for _ in range(int(input('Write count: '))):
    print(next(j), end=' ')

# Ver_2 with StopIteration
def generate_simple_2(m):
    for i in range(2, m):
        if i > 200:
            raise StopIteration()
        if prime(i):
            yield i

j_2 = generate_simple_2(int(input('Write count: ')))
for i in j_2:
    print(i, end=' ')