# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

# Создаем файл для 2 задания

import os

file_path = os.path.join(os.path.dirname(__file__), 'text_file_for_5.2.txt')

with open(file_path, 'w', encoding='utf-8') as obj_1:
    while True:
        user_line = input(f'Введите строку для передачи в файл: ')
        if user_line == '':
            break
        else:
            print(user_line, file=obj_1)
