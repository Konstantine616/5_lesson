# создаем файл для 6го задания

import os

file_path = os.path.join(os.path.dirname(__file__), 'text_file_for_5.6.txt')

try:
    with open(file_path, 'x', encoding='utf-8') as obj_4:
        import_list = ['Информатика:   100(л)   50(пр)   20(лаб)', 'Физика:   30(л)   —   10(лаб)',
                       'Физкультура:   —   30(пр)   —', 'Химия:   90(л)   —   —',
                       'ОБЖ:   —   —  70(лаб)', 'ИЗО:   —   —   —']
        for el in import_list:
            obj_4.write(f'{el}\n')
        print('Запись файла text_file_for_5.6.txt завершена.')
        obj_4.seek(0)
        print('\nСодержимое файла:')
        for read_string in obj_4.readlines():
            print(read_string[:-1])

except FileExistsError:
    print('Файл text_file_for_5.6.txt уже создан.')
    with open('text_file_for_5.6.txt', 'r', encoding='utf-8') as obj_read:
        print('\nСодержимое файла:')
        for read_string in obj_read.readlines():
            print(read_string[:-1])

with open(file_path, 'r', encoding='utf-8') as obj_dict:
    res_dict = {}
    for key in obj_dict.readlines():
        res_dict[key.split()[0][:-1]] = 0
        num = 0
        for el in key.split():
            if el[:el.find('(')].isdigit():
                num += int(el[:el.find('(')])
        res_dict[key.split()[0][:-1]] = num
    print(f'\nРезультат:\n{res_dict}')
