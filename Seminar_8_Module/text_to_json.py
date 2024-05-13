"""Task_1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки."""

# Seminar_73_data_3.txt

import json

def text_to_json(name = 'Seminar_73_data_3.txt'):
    """Создает из текстового файла новый файл с форматом JSON"""
    with ( 
        open(name, 'r', encoding='utf-8') as f,
        open('Seminar_73_data_3.json', 'w', encoding='utf-8') as f2
    ):
        res_list = []
        for line in f:
            res_list.append(line.capitalize())
        json.dump(res_list, f2, indent=4)


if __name__ == '__main__':
    text_to_json()
    