"""Работа с файлами"""

from Seminar_7_Module.extensions_files import generate_with_dictionary, generate_files
from Seminar_7_Module.sort_directory_files import sort_files
from Seminar_7_Module.rename_group_files import rename_files


if __name__ == '__main__':
    d = {
    'doc': 2,
    'jpg': 3,
    'png': 3,
    'txt': 3,
    }
    # Создаем файлы с разными расширениями.
    generate_with_dictionary(d)
    # Генерирует файлы с заданными параметрами.
    generate_files('rnd', 'Seminar_7_data_4', num_files=3)
    # Сортируем файлы по директориям: видео, изображения, текст и т.п.
    sort_files('Seminar_7_data_4')
    # Переименовывает файлы, добавляет порядковый номер 
    rename_files('_new_', 3, 'txt', 'docx', [3, 6], 'Seminar_7_data_4/texts')