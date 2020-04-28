# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников. Пример файла:
# Иванов 23543.12
# Петров 13749.32

from random import random
import os

file_path = os.path.join(os.path.dirname(__file__), 'text_file_for_5.3.txt')

# создаем файл для 3го задания
with open(file_path, 'w', encoding='utf-8') as obj_2:
    import_list = [f'Иванов {random() * (45000 - 5000) + 5000:.2f}', f'Петров {random() * (19999 - 999) + 999:.2f}',
                   f'Пыня {random() * (45000 - 5000) + 5000:.2f}', f'Фирсов {random() * (45000 - 5000) + 5000:.2f}',
                   f'Пеко {random() * (45000 - 5000) + 5000:.2f}', f'Азинов {random() * (45000 - 5000) + 5000:.2f}',
                   f'Фенко {random() * (45000 - 5000) + 5000:.2f}', f'Федко {random() * (45000 - 5000) + 5000:.2f}',
                   f'Ко {random() * (45000 - 5000) + 5000:.2f}', f'Вангуев {random() * (45000 - 5000) + 5000:.2f}']
    for el in import_list:
        obj_2.write(f'{el}\n')

with open(file_path, 'r', encoding='utf-8') as obj:
    print('Сотрудники с зарплатой менее 20000:')
    average = 0.0
    for el in sorted(obj.readlines()):    # делаем сортировку для вывода фамилий в алфовитном порядке
        average += float(el.split()[-1])  # вычисляем общую зарплату
        if float(el.split()[-1]) < 20000:
            print(f'Фамилия: {el.split()[0]:15} Зарплата: {el.split()[-1]}')
    obj.seek(0)
    print(f'Средняя зарплата сотрудников: {average / len(obj.readlines()):.2f}')
