"""Урок 7. Файлы и файловая система"""


"""1. Решить задачи, которые не успели решить на семинаре."""


"""2. Напишите функцию группового переименования файлов. Она должна:
    a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
    b. принимать параметр количество цифр в порядковом номере.
    c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
    d. принимать параметр расширение конечного файла.
    e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
        К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""

from pathlib import Path

def rename_files(new_name, num_digits, old_ext, new_ext, name_range, directory='.'):
    """Переименовывает файлы, добавляет порядковый номер """
    directory = Path(directory)
    for i, file in enumerate(directory.glob(f'*.{old_ext}'), start=1):
        original_name_part = file.stem[name_range[0]:name_range[1]]
        new_file_name = f'{original_name_part}{new_name}{str(i).zfill(num_digits)}.{new_ext}'
        file.rename(directory / new_file_name)

if __name__ == '__main__':
    rename_files('new', 3, 'txt', 'docx', [3, 6], 'Seminar_7_data_4/texts')

"""
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
"""
# Seminar_7_Module = ['extensions_files', 'sort_directory_files', 'pseudonyms_file', 'random_numbers_file', 'pseudonyms_mult_random_numbers_file']