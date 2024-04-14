"""Урок 3. Коллекции"""


"""1. Решить задачи, которые не успели решить на семинаре."""

"""2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов."""

from collections import Counter

list_repeat_number = [1, 2, 3, 2, 3, 2, 3, 4, 3]

# By Counter
dict_by_counter = Counter(list_repeat_number)
print(f'By Counter: {dict_by_counter}')

# By for in + get
dict_count_num = {}
for num in list_repeat_number:
    if num not in dict_count_num.items():
        dict_count_num[num] = dict_count_num.get(num, 0) + 1
print(f'By for in + get: {dict_count_num}\n')

# return
list_return_dublicates = []
for k, v in dict_count_num.items():
    if v > 2:
        list_return_dublicates.append(k)
print(f'Список с дублирующимися элементами: {list_return_dublicates}')


"""3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку."""

text = (
    """В отличие от традиционных энциклопедий, таких как Encyclopædia Britannica, ни одна статья в Википедии не проходит формального процесса экспертной оценки.\
        Любая статья Википедии может редактироваться как с учётной записи участника, так и без регистрации в проекте (за исключением некоторых страниц,\
        подверженных частому вандализму, которые доступны для изменения только определённым категориям участников или, в крайних случаях,\
        только администраторам Википедии), и при этом все внесённые в статью изменения незамедлительно становятся доступными для просмотра любыми пользователями.\
        Поэтому Википедия «не гарантирует истинности» своего содержимого[19],\
        ведь в любом случае между моментом, когда в статью будет внесена какая-то недостоверная информация, и моментом,\
        когда эта информация будет удалена из статьи другим участником Википедии (более компетентным в данной области знания), пройдёт определённое время.\
        (Естественно, для того чтобы обнаружить и удалить из статьи явный вандализм, нужно намного меньше времени,\
        чем для того, чтобы освободить статью от недостоверной информации, когда подобная недостоверность не является особо очевидной.)
    """)

# Ver_1
# удаление символов
new_text = ''
for i in text.lower():
    if i.isalpha() or i.isspace():
        new_text += i
    else:
        new_text += ''

# подсчет слов в словаре
dict_text = {}
for el in new_text.split(' '):
    if el not in dict_text.items() and el != '':
        dict_text[el] = dict_text.get(el, 0) + 1

# сортировка словаря (топ 10)
sorted_dict = sorted(dict_text.items(), key=lambda x: x[1], reverse=True)
print(f'Ver_1 = {sorted_dict[:10]}')

# Ver_2
from collections import Counter
import re

text = text.lower()
# Удаление знаков препинания
words = re.findall(r'\b\w+\b', text)
# Подсчет количества каждого слова
word_counts = Counter(words)
# Возвращение 10 самых часто встречающихся слов
print(f'Ver_2 = {word_counts.most_common(10)}')

"""4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака."""

import random
import math

MAX_WEIGHT = 7
BACKPACK_WEIGHT = 0

hike_things = {
    "палатка" : 2,
    "топор" : 1,
    "стул" : 2,
    "спальник" : 3,
    "котелок" : 2,
    "продукты" : 5,
}

def shuffle_dict(things):
    list_items = list(things.items())
    random.shuffle(list_items)
    return dict(list_items)

shuffle = 0
len_shuffle = math.factorial(len(hike_things.items()))
list_all = []

while len_shuffle > shuffle:
    hike_things_sh = shuffle_dict(hike_things)
    things_to_take = {}
    backpack_weight = BACKPACK_WEIGHT
    for thing in hike_things_sh:
        if thing not in things_to_take and backpack_weight + hike_things_sh[thing] < MAX_WEIGHT:
            things_to_take[thing] = hike_things_sh.get(thing, 0)
            backpack_weight = sum(things_to_take.values())
    list_all.append(things_to_take)
    shuffle += 1

dict_return = []
for el in list_all:
    if el not in dict_return:
        dict_return.append(el)

print('\n Варианты комплектации рюкзака: ')
for i in dict_return:
    print(i)

