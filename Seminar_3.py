'''Урок 3 Коллекции'''

'''Работа со списками

Функция list и квадратные скобки [ ] -Создание списков
Квадратные скобки [ ] -Доступ к элементу по индексу
Метод append() - Добавление одного элемента в конец
Метод extend() - Добавление нескольких элементов в конец
Метод pop() - Удаление элемента по индексу
Метод count() - Подсчёт вхождения элемента
Метод index() - Индекс первого вхождения элемента
Метод insert() - Вставка элемента по индексу
Метод remove() - Удаление элемента по значению

Сортировка:
✔ Функция sorted() + sorted(list, reverse=True) - новый список
✔ Метод sort()
Разворот:
✔ Функция reversed() - новый список
✔ Метод reverse()
✔ Синтаксический сахар [::-1]

Срезы
list[start:stop:step]

Метод copy() - Создаёт поверхностную копию. в матрице изменит оба списка
Функция copy.deepcopy() - Рекурсивно создаёт полную копию

Форматирование строк
Форматирование через %
text = 'my name is %s and I am %d old' % (name, age) -> s - str, d - digit
Метод format()
text = 'my name is {} and I am {} old'.format(name, age)
f-строка
text = f'my name is {} and I am {} old'
f'{num = :_}' -> num = n_nnn_nnn

Строковые методы
Метод split() - Разбивает строку на отдельные элементы 
Метод join() - Формирует строку из отдельных элементов '/'.join(data )
Методы upper(), lower(), title(), capitalize() - Изменение регистра
Методы startswith() и endswith() - Проверка на совпадение с началом или концом строки

Доступ к значению словаря
✔ dict[key] — доступ через квадратные скобки []
✔ dict.get(key[, default]) — доступ через метод get()

Работа со словарями 
Метод setdefault() - Возвращает значение и добавляет ключ в словарь
Метод keys() - возвращает объект-итератор dict_keys
Метод values() - возвращает объект-итератор dict_values
Метод items() - возвращает объект-итератор dict_items
Метод popitem() - Удаляет последнюю пару ключ-значение
Метод pop() - Удаляет пару ключ-значение по ключу
Метод update() - Расширяет исходный словарь новыми парами

Множества
✔ my_set = {1, 2, 3, 4, 2, 5, 6, 7}
Изменяемое множество
✔ my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,))
Неизменяемое множество

Работа с множествами
Метод add() - Добавляет элемент
Метод remove() - Удаляет элемент. выдает ошибку, если элемента в нет.
Метод discard() - Удаляет элемент
Метод intersection() - Пересечение множеств, &
Метод union() - Объединение множеств, |
Метод difference() - Разность множеств, -

'''

"""Task_1
Вручную создайте список с целыми числами, которые повторяются.
Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
*Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.
"""

list_1 = [1, 2, 3, 1, 2,3]
print(list(set(list_1)))

new_list = []
for i in list_1:
    if i not in new_list:
        new_list.append(i)
print(new_list)

"""Task_2
Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
Целое положительное число Вещественное положительное или отрицательное число
Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
Строку в верхнем регистре в остальных случаях
"""

data = input('Input data: \n')
if data.isdecimal():
    print(f'{int(data)} - Целое положительное число')
else:
    try:
        print(f'{float(data)} - Вещественное ')
    except ValueError:
        if data.lower() != data:
            print(f'{data.lower()} - в нижнем регистре')
        else:
            print(f'{data.upper()} - в верхнем регистр')


"""Task_3
Создайте вручную кортеж содержащий элементы разных типов.
Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
"""

tuple_elements = (12, 'line 1', 'line 2', 26.13, 1522, 'line 3')
dict_type = {}
for i in tuple_elements:
    typ = type(i).__name__
    if typ not in dict_type:
        dict_type[typ] = []
    dict_type[typ].append(i)
print(f'{dict_type = }')


"""Task_4
Создайте вручную список с повторяющимися элементами.
Удалите из него все элементы, которые встречаются дважды.
"""
from collections import Counter

list_elements = [1, 1, 1, 5, 4, 7, 7, 8, 9, 9]

# By function Counter 
dict_element_f = Counter(list_elements)
print(f'By function Counter -> {dict_element_f = }')

# By function get
dict_element_g = {}
for el in list_elements:
    dict_element_g[el] = dict_element_g.get(el, 0) + 1
print(f'\t By function get -> {dict_element_g = }')

# By for in
dict_element = {}
for i in list_elements:
    if i not in dict_element:
        dict_element[i] = 0
    dict_element[i] +=1

for k, v in dict_element.items():
    if v == 2:
        list_elements.remove(k)
        list_elements.remove(k)
print(f'\t\t By for in-> {dict_element = }\n')
print(f'By for in -> {list_elements = }')

"""Task_5
Создайте вручную список с повторяющимися целыми числами.
Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
Нумерация начинается с единицы.
"""

list_5 = [1, 2, 3, 1, 2, 3, 7, 8, 9]

new_list_5 = []
for i, el in enumerate(list_5, start=1):
    if el % 2 == 1:
        new_list_5.append(i)
print(f'{new_list_5 = }')

"""Task_6
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
Слова нумеруются начиная с единицы.
Слова выводятся отсортированными согласно кодировки Unicode.
Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
"""

text_6 = input('input text: ').split(' ')
text_6.sort()

max_len = max([len(word) for word in text_6])
max_len_2 = len(max(text_6, key=len))

for i, word in enumerate(text_6, 1):
    print(f'{i}  {word: >{max_len}}')

"""Task_7
Пользователь вводит строку текста.
Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.
"""
from collections import Counter

str_7 = input('Input text: ')
print(Counter(str_7))
dict_7 = {}

for letter in str_7:
    dict_7[letter] = str_7.count(letter)
print(dict_7)

"""Task_8
Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
Какие вещи взяли все три друга
Какие вещи уникальны, есть только у одного друга
Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
Для решения используйте операции с множествами.
Код должен расширяться на любое большее количество друзей.
"""

# ver_1
dict_8 = {
    'Юра': ('палатка', 'рюкзак', 'котелок'),
    'Сергей': ('рюкзак', 'палатка', 'спички', 'лопата'),
    'Олег': ('стол', 'рюкзак', 'продукты'),
}

first = list(dict_8.keys())[0]
res = set(dict_8[first])
for k, v in dict_8.items():
    res = res.intersection(set(v))
print(f'They all have: {res}')

dict_8_count = {}
for k, v in dict_8.items():
    for value in v:
        dict_8_count[value] = dict_8_count.get(value, 0) + 1

friends = len(list(dict_8.keys())) - 1
things = []
for k, v in dict_8_count.items():
    if v == friends:
        things.append(k)

for k, v in dict_8.items():
    for item in things:
        if item not in v:
            print(f'{k} dont have {item} ')
            break

one_thing = []
for k, v in dict_8_count.items():
    if v == 1:
        one_thing.append(k)
print('Only one thing:', *one_thing)     
print(dict_8_count)


# ver_2
hike = {
'Aaz': ("спички", "спальник", "дрова", "топор"),
'Skeeve': ("спальник", "спички", "вода", "еда"),
'Tananda': ("вода", "спички", "косметичка"),
}

at_all = set()
for values in hike.values():
    for value in values:
        at_all.add(value)
print(f'Полный список вещей: {at_all = }')

unique = {}
for master_key, master_values in hike.items():
    for slave_key, slave_values in hike.items():
        if master_key != slave_key:
            if unique.get(master_key):
                unique[master_key] -= set(slave_values)
            else:
                unique[master_key] = set(master_values) - set(slave_values)
print(f'Уникальные вещи: {unique = }')

duplicates = set(at_all)
for value in unique.values():
    duplicates -= value
print(f'Дублирующие вещи: {duplicates = }')
for key, value in hike.items():
    print(f'У {key} отсутствует {(set(value) ^ duplicates) - set(unique[key])}, но есть у остальных')