'''Урок 2 Простые типы данных'''


'''Напишите небольшую программу, которая 
запрашивает у пользователя любой текст 
и выводит о нём следующую информацию:
✔ тип объекта,
✔ адрес объекта в оперативной памяти,
✔ хеш объекта'''

# a = input('print: ')
# print(type(a), id(a), hash(a))

''' print(dir(object)) - содержимое объекта
    help() -> keywords
    help() -> symbols'''

'''Напишите небольшую программу, которая 
запрашивает у пользователя текст. 
Если текст можно привести к целому числу, 
выведите его двоичное, восьмиричное 
и шестнадцатиричное представление. 
А если преобразование к целому невозможно, 
сообщите написан ли текст в ASCII или нет.'''

# text = input('print: ')
# if str.isnumeric(text):
#     text_number = int(text)
#     print(f'двоичное - {bin(text_number)}, восьмиричное - {oct(text_number)} и шестнадцатиричное - {hex(text_number)}')
# else:
#     print(f'преобразование к целому невозможно, текст в ASCII - {str.isascii(text)}')


'''import 
        math
print(dir(math)) - содержимое модуля
print(help(math.gcd)) - инф. о функции gcd
        decimal
num = decimal.Decimal(object) - число с точностью 28 знаков (до и после запятой)
decimal.getcontext().prec = dec - задать точность в dec
        fraction
f1 = fractions.Fraction(1, 3) - представление ввиде дробей 1/3

a = complex(2, 3) - (2+3j), j - мнимая единица
'''

'''print(divmod(10, 3)) - получаем частное и остаток от деления 10/3 = 3 и 1'''

