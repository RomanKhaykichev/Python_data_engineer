"""HW_6_Task_3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь."""

"""HW_6 Task_4. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки"""

import random

def beat_another_queen(queens):
    """Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
    Если ферзи не бьют друг друга возвращает истину, а если бьют - ложь"""
    for i in range(8):
        for j in range(i + 1, 8):
            # Проверяем, находятся ли два ферзя на одной и той же горизонтали, вертикали или диагонали
            if queens[i][0] == queens[j][0] or \
               queens[i][1] == queens[j][1] or \
               abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True


def generate_random_positions():
    """Генерирует случайные позиции"""
    positions = [(i, random.randint(1, 8)) for i in range(1, 9)]
    return positions


def find_valid_queen_positions():
    """Проверяет случайные варианты и выводит 4 успешных расстановки"""
    valid_positions = []
    while len(valid_positions) < 4:
        positions = generate_random_positions()
        if beat_another_queen(positions):
            valid_positions.append(positions)
    return valid_positions

if __name__ == '__main__':
    valid_positions = find_valid_queen_positions()
    for i, positions in enumerate(valid_positions):
        print(f"Успешная расстановка {i+1}: {positions}")