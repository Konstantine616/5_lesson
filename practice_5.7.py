# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.

# создаем файл для 7го задания
from random import randint
import os
import json

file_path = os.path.join(os.path.dirname(__file__), 'text_file_for_5.7.txt')
json_file_path = os.path.join(os.path.dirname(__file__), 'result_file_for_5.7.json')

with open('text_file_for_5.7.txt', 'w+', encoding='utf-8') as obj_7:
    import_list = [f'firm_1   ООО   {randint(5000, 40000)}   {randint(1000, 15000)}',
                   f'firm_2   ООА   {randint(5000, 40000)}   {randint(1000, 15000)}',
                   f'firm_3   ОАО   {randint(5000, 20000)}   {randint(15000, 25000)}',
                   f'firm_4   АОО   {randint(5000, 20000)}   {randint(10000, 20000)}',
                   f'firm_5   ААА   {randint(5000, 45000)}   {randint(15000, 25000)}',
                   f'firm_6   ОАО   {randint(5000, 20000)}   {randint(1000, 15000)}']
    for el in import_list:
        obj_7.write(f'{el}\n')
    print('Запись файла text_file_for_5.7.txt завершена.')
    obj_7.seek(0)
    print('\nСодержимое файла:')
    for read_string in obj_7.readlines():
        print(f'{read_string[:-1]}')

with open('text_file_for_5.7.txt', 'r', encoding='utf-8') as firm_obj:
    profit_firms_dict = {}
    loss_firms_dict = {}
    total_earning = 0
    for string in firm_obj:
        line = string.split()  # Получаем значения фирмы: название, форма собственности, выручка, издержки
        num = int(line[2]) - int(line[-1])  # Вычисляем прибыль фирмы
        if num > 0:                         # Условие для определения в какой словарь попадет фирма
            total_earning += num            # Добавляем прибыль фирмы в общий доход для расчета средней прибыли
            profit_firms_dict[line[0]] = num  # Присваиваем ключу: название фирмы, значению: прибыль
        else:
            loss_firms_dict[line[0]] = num    # Присваиваем ключу: название фирмы, значению: прибыль

    """Получаем словари фирм и средней прибыли"""
    average_profit_dict = {'average_profit': int(total_earning / len(profit_firms_dict.keys()))}
    print(f'\nОбщая прибыль: {total_earning}\nСредняя прибыль: {average_profit_dict["average_profit"]}\n'
          f'Фирмы работающие в плюс:  {profit_firms_dict}\nФирмы работающие в минус: {loss_firms_dict}')
    profit_firms_dict.update(loss_firms_dict)  # Соединяем словари фирм с прибылью и убытком

    """Получаем список словарей"""
    result_list = [profit_firms_dict, average_profit_dict]

    """Записываем преобразованный список в файл формата json"""
    with open(json_file_path, "w+") as json_file:
        json.dump(result_list, json_file)
        json_file.seek(0)
        print(f'\nЧитаем содержимое полученного файла:\n{json_file.read()}')
