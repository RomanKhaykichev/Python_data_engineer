"""Урок 7. Файлы и файловая система"""


"""
- Функция open()
В Python для получения доступа файлу используют функцию open()
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

- Режимы работы с файлами
✔ 'r' — открыть для чтения (по умолчанию)
✔ 'w' — открыть для записи, предварительно очистив файл
✔ 'x' — открыть для эксклюзивного создания. Вернёт ошибку, если файл уже существует
✔ 'a' — открыть для записи в конец файла, если он существует
✔ 'b' — двоичный режим
✔ 't' — текстовый режим (по умолчанию)
✔ '+' — открыты для обновления (чтение и запись)

- Метод close()
✔ f.close()
Если в коде отсутствует метод close(), то даже при успешном завершении 
программы не гарантируется сохранение всех данных в файле

- Прочие необязательные параметры функции open
✔ buffering — определяет режим буферизации
✔ errors — используется только в текстовом режиме и определяет поведение в случае ошибок 
кодирования или декодирования
✔ newline — отвечает за преобразование окончания строки 
✔ closefd — указывает оставлять ли файловый дескриптор открытым при закрытии файла
✔ opener — позволяет передать пользовательскую функцию для открытия файла

- Менеджер контекста with open
with open('text_data.txt', 'r+', encoding='utf-8') as f:
print(list(f))
✔ with гарантирует закрытие файла и сохранение информации

- Чтение файла
list(f)
Чтение в список
res = f.read()
Чтение методом read
res = f.readline()
Чтение методом readline
for line in f:
Чтение циклом for


- Запись и добавление в файл
res = f.write(text)
Запись методом write
f.writelines('\n'.join(text))
Запись методом writelines
print(text, file=f)
print в файл

w
создаём новый пустой файл для записи. 
Если файл существует, открываем его для 
записи и удаляем данные, которые в нём 
хранились
x
создаём новый пустой файл для записи. 
Если файл существует, вызываем ошибку
a
открываем существующий файл для записи 
в конец, добавления данных. Если файл 
не существует, создаём новый файл 
и записываем в него

- Методы перемещения в файле
f.tell()
Метод tell возвращает текущую 
позицию в файле

seek(offset, whence=0)
offset — смещение относительно 
опорной точки,
whence — способ выбора 
опороной точки.
✔ whence=0 — отсчёт 
от начала файла
✔ whence=1 — отсчёт от 
текущей позиции в файле 
✔ whence=2 — отсчёт 
от конца файла

truncate(size=None)
Метод изменяет размер файла. 
Если не передать значение 
в параметр size будет удалена 
часть файла от текущей позиции 
до конца


- Файловая система - 

from pathlib import Path

Для получения информации о текущем каталоге м
print(Path.cwd())
Для создания каталога
Path('new_path_dir').mkdir()
Для удаления одного каталога
Path('some_dir/dir/new_path_dir').rmdir()
Если необходимо удалить каталог со всем его содержимым
import shutil
shutil.rmtree('dir/other_dir')
shutil.rmtree('some_dir')
Формирование пути
file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')

Переименование файлов
Path('new_file.py').rename('newest_file.py')
Перемещение файлов
old_file = Path('new_name.py')
new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)
Копирование файлов
import shutil
shutil.copy('one.txt', 'dir')
shutil.copy2('two.txt', 'dir')
скопировать каталог
import shutil
shutil.copytree('dir', 'one_more_dir')
Удаление файлов
Path('one_more_dir/one_more.txt').unlink()
удаления всего каталога
import shutil
shutil.rmtree('dir')
"""

"""Task_1
Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.
"""

import os
import random as rd

MIN_NUMBER = -1000
MAX_NUMBER = 1000


def generate_number_file(count: int, file_name: str):
    """функциюя заполняет файл случайными числами"""
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(count):
            f.write(f'{rd.randint(MIN_NUMBER, MAX_NUMBER)} | {rd.random() * 2000 - 1000}')
            f.write('\n' if i < count - 1 else '')


if __name__ == '__main__':
    generate_number_file(10, "Seminar_71_data_1.txt")

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

"""Task_3
Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла, возвращайтесь в его начало.
"""


def read_line_or_begin(fd) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text[:-1]


def process_files(file_numbers, file_names, file_res):
    """Сохраняет имя из файла с именами и перемножение чиисел из файла с числами"""
    with (
        open(file_numbers, 'r', encoding='utf-8') as f_num,
        open(file_names, 'r', encoding='utf-8') as f_names,
        open(file_res, 'w', encoding='utf-8') as f_res
        ):
        length1 = len(f_num.readlines())
        length2 = len(f_names.readlines())
        length = max(length1, length2)
        for i in range(length):
            line_num = read_line_or_begin(f_num)
            line_name = read_line_or_begin(f_names)
            a, b = line_num.split('|')
            a = int(a)
            b = float(b)
            res = a * b
            if res < 0:
                res *= -1
                line_name = line_name.lower()
            else:
                res = round(res)
                line_name = line_name.upper()
            f_res.write(f'{line_name} {res}')
            f_res.write('\n' if i < length - 1 else "")


if __name__ == '__main__':
    process_files('Seminar_71_data_1.txt', 'Seminar_72_data_2.txt', 'Seminar_73_data_3.txt')

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
        with open(f'{directory}/{filename}.{extension}', 'w', encoding='utf-8') as f:
            f.write(text)


if __name__ == '__main__':
    generate_files('rnd', 'Seminar_7_data_4')


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
    d = {
    'doc': 5,
    'jpg': 10,
    'png': 23,
    'txt': 15,
    }
    generate_with_dictionary(d)


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
        while True:
            try:
                with open(f'{directory}/{filename}.{extension}', 'x', encoding='utf-8') as f:
                    f.write(text)
            except:
                filename = generate_text(name_length)
            else:
                break


if __name__ == '__main__':
    generate_files('rnd', 'Seminar_7_data_4')

"""Task_7
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""

import os

DICTIONARY = {
    'doc': 'texts',
    'txt': 'texts',
    'jpg': 'pictures',
    'png': 'pictures',
}

def sort_files(directory):
    """Сортирует файлы по директориям: видео, изображения, текст и т.п."""
    for f in os.listdir(directory):
        extension = f.rsplit('.')[-1]
        if extension not in DICTIONARY:
            continue
        new_directory = f'{directory}/{DICTIONARY[extension]}'
        if not os.path.exists(new_directory) or not os.path.isdir(new_directory):
            os.mkdir(new_directory)
        os.rename(f'{directory}/{f}',
                  f'{new_directory}/{f}')


if __name__ == '__main__':
    sort_files('Seminar_7_data_4')
