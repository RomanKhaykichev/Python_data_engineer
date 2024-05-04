"""Task_3
Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла, возвращайтесь в его начало.
"""


def read_line_or_begin(fd) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text[:-1]


def process_files(file_numbers, file_names, file_res):
    """Сохраняет имя из файла с именами и перемножение чиисел из файла с числами"""
    with (
        open(file_numbers, 'r', encoding='utf-8') as f_num,
        open(file_names, 'r', encoding='utf-8') as f_names,
        open(file_res, 'w', encoding='utf-8') as f_res
        ):
        length1 = len(f_num.readlines())
        length2 = len(f_names.readlines())
        length = max(length1, length2)
        for i in range(length):
            line_num = read_line_or_begin(f_num)
            line_name = read_line_or_begin(f_names)
            a, b = line_num.split('|')
            a = int(a)
            b = float(b)
            res = a * b
            if res < 0:
                res *= -1
                line_name = line_name.lower()
            else:
                res = round(res)
                line_name = line_name.upper()
            f_res.write(f'{line_name} {res}')
            f_res.write('\n' if i < length - 1 else "")


if __name__ == '__main__':
    process_files('Seminar_71_data_1.txt', 'Seminar_72_data_2.txt', 'Seminar_73_data_3.txt')