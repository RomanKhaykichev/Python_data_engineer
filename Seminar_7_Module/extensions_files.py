"""Task_4
Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
расширение минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.
"""

"""Task_6
Дорабатываем функции из предыдущих задач.
Генерируйте файлы в указанную директорию — отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""

import random
import os

MIN_LETTER = ord('a')
MAX_LETTER = ord('z')

def generate_text(length):
    """Генерирует случайное имя файла."""
    name = []
    for i in range(length):
        name.append(chr(random.randint(MIN_LETTER, MAX_LETTER)))
    return "".join(name)


def generate_files(extension:str,
                   directory: str,
                   min_length=6,
                   max_length=30,
                   min_bytes=256,
                   max_bytes=4096,
                   num_files=42):
    """Генерирует файлы с заданными параметрами."""
    if not os.path.exists(directory) or not os.path.isdir(directory):
        os.mkdir(directory)
    for i in range(num_files):
        name_length = random.randint(min_length, max_length)
        filename = generate_text(name_length)
        text_length = random.randint(min_bytes, max_bytes)
        text = generate_text(text_length)
        while True: # Task_6
            try:
                with open(f'{directory}/{filename}.{extension}', 'x', encoding='utf-8') as f:
                    f.write(text)
            except:
                filename = generate_text(name_length)
            else:
                break


"""Task_5
Доработаем предыдущую задачу.
Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи.
"""


def generate_with_dictionary(dictionary: dict):
    """Генерирует с файлы с заданным расширением"""
    for key, value in dictionary.items():
        generate_files(key, 'Seminar_7_data_4', num_files=value)


if __name__ == '__main__':
    generate_files('rnd', 'Seminar_7_data_4')

if __name__ == '__main__':
    d = {
    'doc': 5,
    'jpg': 10,
    'png': 23,
    'txt': 15,
    }
    generate_with_dictionary(d)