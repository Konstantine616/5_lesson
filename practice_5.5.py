# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import os

file_path = os.path.join(os.path.dirname(__file__), 'result_file_for_5.5.txt')

with open(file_path, 'w+') as obj:
    num_list = []
    i = 1
    while True:
        num = input(f'Введите {i}-е число для записи в файл:\n')
        if num.isdigit():
            num_list.append(num)
            i += 1
        else:
            print('Вы ввели иной символ, запись чисел завершена.')
            break
    obj.write(' '.join(num_list))
    obj.seek(0)

    sum_num = 0
    for el in obj.readline().split():
        sum_num += int(el)
    print(f'Сумма чисел {" + ".join(num_list)} = {sum_num}')
