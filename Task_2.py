'''Урок 2. Простые типы данных'''


'''1. Решить задачи, которые не успели решить на семинаре.'''

'''2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.'''

BASE = 16

def number_hex(number):
    digits = '0123456789abcdef'
    result = ''
    while number > 0:
        result += digits[number % BASE]
        number //= BASE
    return print(result[::-1] or '0')

number = int(input('Number: '))
number_hex(number)
print(hex(number))

'''3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions'''

import fractions
import math

def str_to_int(str_fraction: str):
    '''перевод строки на числовой числитель и знаменатель'''
    split_str_fraction = str_fraction.split('/')
    numerator = int(split_str_fraction[0])
    denominator = int(split_str_fraction[1])
    return numerator, denominator
    
def sum_fraction(frac_1, frac_2):
    '''сумма дробей'''
    num_1, denom_1 = str_to_int(frac_1)
    num_2, denom_2 = str_to_int(frac_2)
    num_3 = num_1 * denom_2 + num_2 * denom_1
    denom_3 = denom_1 * denom_2
    gcd = math.gcd(num_3, denom_3)
    return  f'{int(num_3 / gcd)}/{int(denom_3 / gcd)}'

def multiplication_fraction(frac_1, frac_2):
    '''умножение дробей'''
    num_1, denom_1 = str_to_int(frac_1)
    num_2, denom_2 = str_to_int(frac_2)
    num_3 = num_1 * num_2
    denom_3 = denom_1 * denom_2
    gcd = math.gcd(num_3, denom_3)
    return f'{int(num_3 / gcd)}/{int(denom_3 / gcd)}'  

def check_correct(frac_1, frac_2):
    '''проверка на корректность написания дроби'''
    if frac_1[0].isdigit() and frac_1[1] == '/' and frac_1[2].isdigit() \
        and frac_2[0].isdigit() and frac_2[1] == '/' and frac_2[2].isdigit():
        return True
    else:
        print('Ввели дробь не по условию!')


fraction_1 = input('Введите дробь в формате a/b: ')
fraction_2 = input('Введите дробь в формате a/b: ')

check_correct(fraction_1, fraction_2)
num_1, denum_1 = str_to_int(fraction_1)
num_2, denum_2 = str_to_int(fraction_2) 
frac_1 = fractions.Fraction(num_1, denum_1)
frac_2 = fractions.Fraction(num_2, denum_2)

print(f'Sum: {sum_fraction(fraction_1, fraction_2)}')
print(f'Check by Fraction: {frac_1 + frac_2}')
print(f'Multiplication: {multiplication_fraction(fraction_1, fraction_2)}')
print(f'Check by Fraction: {frac_1 * frac_2}')