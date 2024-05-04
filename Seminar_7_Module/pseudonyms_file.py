"""Task_2
Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
Полученные имена сохраните в файл.
"""

import random

MIN_LEN = 4
MAX_LEN = 7
MIN_LETTER = ord('a')
MAX_LETTER = ord('z')
VOWELS = ('a', 'o', 'y', 'i', 'u', 'e')


def generate_name(file_name: str, count_name:int):
    """Функция генерирует псевдоимена."""
    with open(file_name, 'w', encoding='utf-8') as f:
        for j in range(count_name):
            len_name = random.randint(MIN_LEN, MAX_LEN)
            name = []
            for i in range(len_name):
                name.append(chr(random.randint(MIN_LETTER, MAX_LETTER)))
            has_vowels = False
            for letter in name:
                if letter in VOWELS:
                    has_vowels = True
                    break
            if not has_vowels:
                ind = random.randint(0, len_name - 1)
                letter = random.choice(list(VOWELS))
                name[ind] = letter
            print(f'{"".join(name).capitalize()}', file=f, end='')
            f.write('\n' if j < count_name - 1 else '')


if __name__ == '__main__':
    generate_name('Seminar_72_data_2.txt', 15)