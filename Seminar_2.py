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


'''Task_1
Создайте несколько переменных разных типов.
Проверьте к какому типу относятся созданные переменные.
'''
a = 13
b = 5.1
c = 'hello'
d = {a, b, c}
e = [a, b, c]
f = {a:1, b:2}
print(type(a),type(b), type(c), type(d), type(e), type(f))

'''Task_2
Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок.
Для каждого элемента в цикле выведите: порядковый номер начиная с единицы значение адрес в памяти размер в памяти
хэш объекта результат проверки на целое число только если он положительный
результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты
'''

from sys import getsizeof
from typing import Hashable

data = [1, 'row', 5.11, [1, 2], {2, 3}]
for number, i in enumerate(data, start=1):
    print(number, end='\t' )
    print(i, end='\t' )
    print(id(i), end='\t')
    print(getsizeof(i), end='\t')
    if isinstance(i, Hashable):
        print(hash(i), end='\t')
    if isinstance(i, int):
        print('целое число', end='\t')
    if isinstance(i, str):               # if type(i) == str:
        print('строка', end='\t')
    print('')

'''Task_3
Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
Функции bin и oct используйте для проверки своего результата, а не для решения.
Дополнительно:
Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
Избегайте магических чисел. Добавьте аннотацию типов где это возможно'''

BASE = 2 # 8 для восьмеричной

number = int(input('Number: '))
if BASE == 2:
    print(bin(number))
if BASE == 8:
    print(oct(number))

result = ''
while number >= BASE:
    result += str(number % BASE)
    number //= BASE
result += str(number)
print(result[::-1])

'''Task_4
Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
Диаметр не превышает 1000 у.е. Точность вычислений должна составлять не менее 42 знаков после запятой.
'''
import decimal
import math

decimal.getcontext().prec = 50
d = decimal.Decimal(input('Diametr < 1000: '))
r = d / 2
pi = decimal.Decimal(math.pi)
s = pi * r ** 2
long = 2 * pi * r
print(s, long)

'''Task_5
Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
Используйте комплексные числа для извлечения квадратного корня.
'''

a = int(input('print a: '))
b = int(input('print b: '))
c = int(input('print c: '))

d = b ** 2 - 4 * a * c
if d > 0:
    print((-b + d ** 0.5) / (2 * a))
    print((-b - d ** 0.5) / (2 * a))
elif d == 0:
    print((-b) / (2 * a))
else:
    d = complex(d)
    print((-b + d ** 0.5) / (2 * a))
    print((-b - d ** 0.5) / (2 * a))
    
'''Task_6
Напишите программу банкомат.
Начальная сумма равна нулю. Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег
'''

from decimal import Decimal

MIN_SUM = 50
PROCENT_COMMISION = Decimal(0.015)
MIN_COMISSION = 30
MAX_COMISSION = 600
BONUS = Decimal(0.03)
LIMIT_BEFORE_TAX = 5_000_000
TAX_BATE = Decimal(0.1)


def menu(balance: Decimal, count: int, is_flag: bool):
    dct = {'1': 'Пополнить счет',
            '2': 'Снять со счета',
            '3': 'Выйти из программы'}
    
    for k, v in dct.items():
        if k.isdigit():
            print(f'{k}: {v}')
        else:
            print(v)
    if balance > LIMIT_BEFORE_TAX:
        balance *= (1 - TAX_BATE)
    choice = input('Выберите команду: ')
    if choice == '3':
        print(balance)
        is_flag = False
        return balance, is_flag
    elif choice == '1':
        balance = give_money(balance)
        count += 1
    elif choice == '2':
        balance = get_money(balance)
        count += 1
    else:
        print('Неверная команда: ')
    if count % 3 == 0:
        balance = (1 + BONUS)
    print(balance)
    return balance, is_flag

def get_money(balance: Decimal):
    money_to_get = Decimal(input('Введите сумму снятия: '))
    procent = money_to_get * PROCENT_COMMISION

    if money_to_get % MIN_SUM == 0:
        if procent < MIN_COMISSION:
            procent = MIN_COMISSION
        elif procent > MAX_COMISSION:
            procent = MAX_COMISSION
        
        if money_to_get + procent <= balance:
            return balance - (money_to_get + procent)
        else:
            print('Недостаточно средств')
            return balance
    else:
        print('Ошибка снятия денег, сумма должна быть кратной 50')
        return balance

def give_money(balance: Decimal):
    money_to_give = Decimal(input('Введите сумму пополнения: '))

    if money_to_give % MIN_SUM == 0:
        return balance + money_to_give
    else:
        print('Ошибка пополнения денег, сумма должна быть кратной 50')
        return balance

if __name__ == '__main__':
    print('Добро пожаловать в программу банкомат! ')
    balance = 0
    count = 1
    is_flag = True
    while is_flag:
        balance, is_flag = menu(balance, count, is_flag)
        