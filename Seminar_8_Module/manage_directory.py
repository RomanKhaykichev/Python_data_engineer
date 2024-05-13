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