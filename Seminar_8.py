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

import json

def text_to_json(name = 'Seminar_73_data_3.txt'):
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
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
"""

import json


def json_to_csv(name='Seminar_82_db.json', res_file='Seminar_83_db.csv'):
    with open(name, 'r', encoding='utf-8') as f_json:
        db = json.load(f_json)
    with open(res_file, 'w', encoding='utf-8') as f:
        for k, v in db.items():
            for k2, v2 in v.items():
                print(f'{k}, {k2}, {v2}', file=f)


if __name__ == '__main__':
    json_to_csv()

"""Task_4
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями. В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
"""

import csv
import json
from pathlib import Path


def csv2json(from_file: Path, to_file: Path) -> None:
    json_list = []
    with open(from_file, 'r', newline='', encoding='utf-8') as f:
        csv_write = csv.reader(f, dialect='excel')
        for i, line in enumerate(csv_write):
            json_dict = {}
            if i == 0: # если есть заголовки
                continue
            else:
                level, id, name = line
                json_dict['level'] = int(level)
                json_dict['id'] = f"{int(id):010}"
                json_dict['name'] = name.title()
                json_dict['hash'] = hash(f"{json_dict['name']}{json_dict['id']}")
                json_list.append(json_dict)

    with open(to_file, 'w', encoding='utf-8') as f:
        json.dump(json_list, f, indent=2)


if __name__ == '__main__':
    csv2json(Path('Seminar_83_db.csv'), Path('Seminar_84_db_csv.json'))


"""Task_5
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.
"""

import json
import pickle
import os

def json_to_pickle(directory='.'):
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

"""Task_6
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""

import csv
import pickle
from pathlib import Path


def pickle2csv(file: Path) -> None:
    with (
        open(file, 'rb') as f_read,
        open(f'{file.stem}_2.csv', 'w', newline='', encoding='utf-8') as f_write,
    ):
        data = pickle.load(f_read)

        keys = list(data[0].keys())
        csv_write = csv.DictWriter(f_write, fieldnames=keys, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)

        csv_write.writeheader()
        csv_write.writerows(data)


if __name__ == '__main__':
    pickle2csv(Path('Seminar_84_db_csv.pickle'))

"""Task_7
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Распечатайте его как pickle строку.
"""

import csv
import pickle
from pathlib import Path


def csv2pickles(file: Path) -> None:
    pickle_list = []
    with open(file, 'r', newline='', encoding='utf-8') as f:
        csv_file = csv.reader(f, dialect='excel')
        for i, line in enumerate(csv_file):
            if i == 0:
                pickle_keys = line
            else:
                pickle_dict = {k: v for k, v in zip(pickle_keys, line)}
                pickle_list.append(pickle_dict)

    print(pickle.dumps(pickle_list))


if __name__ == '__main__':
    csv2pickles(Path('Seminar_84_db_csv_2.csv'))
