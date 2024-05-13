"""Урок 8. Сериализация"""

"""1. Решить задачи, которые не успели решить на семинаре."""

"""
2. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
    ○ Для дочерних объектов указывайте родительскую директорию.
    ○ Для каждого объекта укажите файл это или директория.
    ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""

import os
import json
import csv
import pickle

def get_size(start_path = '.'):
    """Возвращает размер в байтах"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def walk_dir(dir_path):
    """Рекурсивно обходит директорию и сохраняет данные о файлах"""
    data = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            file_path = os.path.join(root, name)
            size = os.path.getsize(file_path)
            data.append({"type": "file", "name": name, "parent_directory": root, "size_bytes": size})
        for name in dirs:
            dir_path = os.path.join(root, name)
            size = get_size(dir_path)
            data.append({"type": "directory", "name": name, "parent_directory": root, "size_bytes": size})
    return data


def save_data(data, dir_path):
    """Сохраняет в файлы json, csv и pickle."""
    with open(os.path.join(dir_path, 'Task_82_data.json'), 'w') as f:
        json.dump(data, f)
    with open(os.path.join(dir_path, 'Task_82_data.csv'), 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    with open(os.path.join(dir_path, 'Task_82_data.pkl'), 'wb') as f:
        pickle.dump(data, f)


def manage_directory(directory='.'):
    """Сохраняет данные и размер файлов из директрории в формат json, csv и pickle."""
    data = walk_dir(directory)
    save_data(data, directory)


if __name__ == '__main__':
    manage_directory()


"""3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов."""

"""Работа с файлами разных форматов - Seminar_8_Module"""

from Seminar_8_Module.text_to_json import text_to_json # Создает из текстового файла новый файл с форматом JSON"
from Seminar_8_Module.access_users import access_users # Добавляет введенные пользователем данные в JSON файл
from Seminar_8_Module.json_to_csv import json_to_csv # Создает из файла JSON новый файл с форматом CSV
from Seminar_8_Module.csv_to_json import csv2json # Создает из файла CSV новый файл с форматом JSON
from Seminar_8_Module.json_to_pickle import json_to_pickle # "Создает из файла JSON новый файл с форматом pickle
from Seminar_8_Module.pickle_to_csv import pickle2csv # Создает из файла pickle новый файл с форматом csv
from Seminar_8_Module.csv_to_print_pickle import csv2pickles # Выводит как pickle строку данные из файла форматом CSV
from Seminar_8_Module.manage_directory import manage_directory # Сохраняет данные и размер файлов из директрории в формат json, csv и pickle.
