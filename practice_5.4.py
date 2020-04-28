# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import os

file_path = os.path.join(os.path.dirname(__file__), 'text_file_for_5.4.txt')
file2_path = os.path.join(os.path.dirname(__file__), 'result_file_for_5.4.txt')

with open(file_path, 'r', encoding='utf-8') as obj:
    rus_dict = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре', '5': 'Пять',
                '6': 'Шесть', '7': 'Семь', '8': 'Восемь', '9': 'Девять', '0': 'Ноль'}

    with open(file2_path, 'w+', encoding='utf-8') as res_obj:
        for string in obj:
            new_string = string.split()
            for key, val in rus_dict.items():
                if string.split()[2] == key:
                    new_string[0] = val
                    res_obj.write(f"{' '.join(new_string)}\n")
                    print(f'{string[:-1]} ——> {" ".join(new_string)}')
