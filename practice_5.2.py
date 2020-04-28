# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

import os

file_path = os.path.join(os.path.dirname(__file__), 'text_file_for_5.2.txt')
with open(file_path, 'r', encoding='utf-8') as obj:
    for ind, el in enumerate(obj.readlines(), 1):
        """Считаем кол-во строк и слов в строке"""
        print(f'В {ind} строке {len(el.split())} слов(а);', end=' ')
        for i, word in enumerate(el.split(), 1):
            """Считаем кол-во символов в каждом слове"""
            print(f'в(во) {i}-ом слове {len(word)} символа(ов),', end=' ')
        print(f'\n{el[:-1]}')
