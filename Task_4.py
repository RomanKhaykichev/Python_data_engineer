"""Урок 4. Функции"""

"""
1. Напишите функцию для транспонирования матрицы
"""


def transpose_matrix(matrix: list[list]) -> list[list]:
    """возвращает транспонированную матрицу"""
    return [[row[elem] for row in matrix] for elem in range(len(matrix[0]))]


def print_matrix(matrix: list[list]) -> print:
    """печатает матрицу"""
    return [print(' '.join(str(elem) for elem in row)) for row in matrix]


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 2, 1], [5, 2, 3]]
    print_matrix(matrix)
    print()
    print_matrix(transpose_matrix(matrix))


"""
2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""


def add_kwargs_dict(**kwargs) -> dict:
    """Добавляет ключевые параметры в словарь
    
    : ключ — значение переданного аргумента,
    : значение — имя аргумента.
    """
    result = {}
    for key, value in kwargs.items():
        try:
            hash(value)
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result


if __name__ == '__main__':
    print(add_kwargs_dict(x=5, y=2, z=3, a=1, b=2.5, c='text'))

"""
3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

from decimal import Decimal

MIN_SUM = 50
PROCENT_COMMISION = Decimal(0.015)
MIN_COMISSION = 30
MAX_COMISSION = 600
BONUS = Decimal(0.03)
LIMIT_BEFORE_TAX = 5_000_000
TAX_BATE = Decimal(0.1)


def menu(balance: Decimal, count: int, transaction_lst: list, is_flag: bool):
    """вызвать меню"""
    dct = {'1': 'Пополнить счет',
            '2': 'Снять со счета',
            '3': 'Выйти из программы'}
    for k, v in dct.items():
        if k.isdigit():
            print(f'{k}: {v}')
        else:
            print(v)
    if balance > LIMIT_BEFORE_TAX:
        transaction_lst.append(f'Снятие комиссии - {balance * (1 - TAX_BATE)}')
        balance *= (1 - TAX_BATE)
    choice = input('Выберите команду: ')
    if choice == '3':
        print(balance)
        print(*transaction_lst, sep='\n')
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
        transaction_lst.append(f'Начисление бонуса + {balance * (1 + BONUS)}')
        balance = (1 + BONUS)
    print(balance)
    return balance, is_flag


def get_money(balance: Decimal):
    """рассчитывает комиссию и выдает сумму денег"""
    money_to_get = Decimal(input('Введите сумму снятия: '))
    procent = money_to_get * PROCENT_COMMISION

    if money_to_get % MIN_SUM == 0:
        if procent < MIN_COMISSION:
            procent = MIN_COMISSION
        elif procent > MAX_COMISSION:
            procent = MAX_COMISSION
        
        if money_to_get + procent <= balance:
            transaction_lst.append(f'Снятие со счета - {money_to_get + procent} - комиссия {procent}%')
            return balance - (money_to_get + procent)
        else:
            print('Недостаточно средств')
            return balance
    else:
        print('Ошибка снятия денег, сумма должна быть кратной 50')
        return balance


def give_money(balance: Decimal):
    """зачисляет наличные на счет"""
    money_to_give = Decimal(input('Введите сумму пополнения: '))

    if money_to_give % MIN_SUM == 0:
        transaction_lst.append(f'Пополнение счета + {money_to_give}')
        return balance + money_to_give
    else:
        print('Ошибка пополнения денег, сумма должна быть кратной 50')
        return balance


if __name__ == '__main__':
    print('Добро пожаловать в программу банкомат! ')
    balance = 0
    count = 1
    is_flag = True
    transaction_lst = []
    while is_flag:
        balance, is_flag = menu(balance, count, transaction_lst, is_flag)
