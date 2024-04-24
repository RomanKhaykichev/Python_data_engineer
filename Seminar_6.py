"""Урок 6. Модули"""

"""
- Простой импорт
import sys

print(sys)
print(sys.builtin_module_names)
print(*sys.path, sep='\n')

- Абсолютный импорт
import from
from sys importn builtin_module_names

import as
import numpy as np

✔ from имя_модуля import *
Подобная запись импортирует из модуля все 
глобальные объекты за исключением тех, чьи 
имена начинаются с символа подчёркивания.

Переменная __all__
✔ __all__ = ['func', '_secret', '...']
Cписок имён объектов, заключённых в кавычки, т.е. строки для импорта через «звёздочку».

- Относительный импорт
from . import other_module
from .. import other_module
from ..other_package import
other_module


Создание пакетов и их импорт

Файл __init__.py
Директоия с __init__.py превращается в пакет

Модуль sys и запуск скрипта с параметрами
from sys import argv
print('start')
print(argv)
print('stop')
Команда запуска:
python script.py -d 42 -s "Hello world!" -k 100

Модуль random
Модуль используется для генерации псевдослучайных чисел.
✔ random() — генерирует псевдослучайные числа в диапазоне [0, 1)
✔ seed(a=None, version=2) — инициализирует генератор. Если значение 
a не указано, для инициализации используется текущее время ПК
✔ getstate() — возвращает объект с текущим состоянием генератора
✔ setstate(state) — устанавливает новое состоянии генератора, 
принимая на вход объект, возвращаемый функцией getstate

randint(a, b) - целое число от a до b
uniform(a, b) - вещественное число от a до b
choice(seq) - случайный элемент последовательности
randrange(start, stop[, step]) - число из диапазона
shuffle(x) - перемешиваем коллекцию x in place
sample(population, k, *, counts=None) - Выборка в k элементов из population
"""


