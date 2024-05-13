"""Task_5
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.
"""

import json
import pickle
import os

def json_to_pickle(directory='.'):
    """Создает из файла JSON новый файл с форматом pickle"""
    for file in os.listdir(directory):
        file_name, file_extension = os.path.splitext(file)
        # print(file_extension)
        if file_extension == '.json':
            with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
                data = json.load(f)
            with open(os.path.join(directory, file_name + '.pickle'), 'wb') as f_pickle:
                pickle.dump(data, f_pickle)


if __name__ == '__main__':
    json_to_pickle()