"""Урок 8. Сериализация"""


"""
- Сериализация данных

Сериализация — это процесс преобразования объекта в поток байтов для сохранения или передачи в память, базу данных или файл.

Десериализация – восстановление объектов из байт, сохранение которых было произведено ранее.
Процедура выгрузки «зафиксированной» информации пользователем.

- Преобразование JSON (JavaScript Object Notation) в Python
import json
● json_file = json.load(f)
загрузка JSON из файла и сохранение в dict или list
● json_list = json.loads(json_text)
загрузка JSON из строки и сохранение в dict или list


- Преобразование Python в JSON

import json
● json.dump(my_dict, f)
сохранение dict или list в файле в виде JSON
● dict_to_json_text = json.dumps(my_dict) # = json.dumps(my_dict, ensure_ascil=False) - сохпанение на русском
сохранение dict или list в виде JSON строки


- Дополнительные параметры dump и dumps
res = json.dumps(my_dict, indent=2,
                            separators=(',', ':'),
                            sort_keys=True)
● Параметр indent отвечает за форматирование с отступами
● Параметр separators принимает на вход кортеж из двух строковых элементов. 
Первый — символ разделитель элементов.
Второй — разделитель ключа и значения.
● Параметр sort_keys отвечает за сортировку ключей по алфавиту


- CSV (Comma-Separated Values)

CSV — текстовый формат, предназначенный для представления 
табличных данных. Строка таблицы соответствует строке текста, 
которая содержит одно или несколько полей, разделенных запятыми. 
"Name","Sex","Age","Height (in)","Weight (lbs)"
"Alex","M",41,74,170
"Bert","M",42,68,166
"Carl","M",32,70,155

Чтение CSV
import csv
● with open('biostats.csv', 'r', newline='') as f:
параметр newline='' для работы с CSV
● csv_file = csv.reader(f)
csv_file позволяет построчно читать csv файл в список list

Запись CSV
import csv
● csv_write = csv.writer(f)
csv_write позволяет сохранять данные в формате CSV
● csv_write.writerow(line)
сохранение списка в одной строке файла в формате CSV
● csv_write.writerows(all_data)
сохранение матрицы в нескольких строках файла в формате CSV

Чтение CSV в словарь
csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age",
"height", "weight", "office"], restkey="new", restval="Main Office")
● fieldnames — список заголовков столбцов, ключей словаря
● restkey — значение ключа для столбцов, которых нет в fieldnames 
● restval — значение поля для ключей fieldnames, которых нет в файле CSV

Запись CSV из словаря
import csv
● Параметры класса DictWriter аналогичны параметрам DictReader
● csv_write.writeheader()
сохранение первой строки с заголовками в порядке их 
перечисления в параметре fieldnames
● csv_write.writerow(line)
сохранение списка в одной строке файла в формате CSV
● csv_write.writerows(all_data)
сохранение матрицы в нескольких строках файла в формате CSV


- Модуль Pickle

Модуль pickle не занимается проверкой потока байт на безопасность перед распаковкой.
Не используйте его с тем набором байт, безопасность которого не можете гарантировать.
import pickle
res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
print(res)

import pickle
● pickle.dump(my_dict, f)
сохранение объекта в бинарном файле 
● result = pickle.dumps(my_dict)
сохранение объекта в строку байт

Десериализация
● new_dict = pickle.load(f)
загрузка из бинарного файла и сохранение в объекта
● new_dict = pickle.loads(data)
получение объекта из бинарной строки
"""

"""Task_1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки."""
# Seminar_73_data_3.txt

# import json

# def text_to_json(name = 'Seminar_73_data_3.txt'):
#     with ( 
#         open(name, 'r', encoding='utf-8') as f,
#         open('Seminar_73_data_3.json', 'w', encoding='utf-8') as f2
#     ):
#         res_list = []
#         for line in f:
#             res_list.append(line.capitalize())
#         json.dump(res_list, f2, indent=4)


# if __name__ == '__main__':
#     text_to_json()

"""Task_2
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""

import json
import os


def access_users(name='Seminar_82_db.json'):
    db = {}
    if os.path.exists(name) and os.path.isfile(name):
        with open(name, 'r', encoding='utf-8') as f:
            db = json.load(f)
    with open(name, 'w', encoding='utf-8') as f:
        while True:
            while True:
                try:
                    user_level = int(input("Write you level (1-7) or text to exit: "))
                except:
                    json.dump(db, f)
                    exit()
                else:
                    break
            if not 1 <= user_level <=7:
                continue
            if user_level not in db:
                db[user_level] = {}
            while True:
                try:
                    user_id = int(input('Write your id: '))
                except:
                    print('Uncorrect, it is not a number')
                else:
                    flag = False
                    for level in db:
                        for ident in db[level]:
                            if ident == user_id:
                                print('Id must be unique!')
                                flag = True
                                break
                    if flag:
                        continue
                    else:
                        break
            while True:
                user_name = input('Write your name: ')``
                if user_name:
                    break
                else:
                    print('You dont write name!')
            db[user_level][user_id] = user_name
        

if __name__ == '__main__':
    access_users()

"""Task_3


"""
