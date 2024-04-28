"""Урок 6. Модули"""


"""1. Решить задачи, которые не успели решить на семинаре."""

"""2. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""

# Seminar_6_Module - leap_year.py
from Seminar_6_Module.leap_year import check_day
from sys import argv

if __name__ == '__main__':
    if len(argv) == 2:
        print(check_day(argv[1]))
    else:
        print(check_day(input('Введено не корректно. Введите дату чч.мм.гггг: ')))

"""3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь."""

# Seminar_6_Module - chess.py
from Seminar_6_Module.chess import beat_another_queen

if __name__ == '__main__':
    queens = [(2, 3), (2, 1), (1, 3), (2, 5), (3, 1), (5, 6), (3, 4), (5, 1)]
    print(beat_another_queen(queens))

"""4. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки"""

# # Seminar_6_Module - chess.py
from Seminar_6_Module.chess import find_valid_queen_positions

if __name__ == '__main__':
    valid_positions = find_valid_queen_positions()
    for i, positions in enumerate(valid_positions):
        print(f"Успешная расстановка {i+1}: {positions}")
