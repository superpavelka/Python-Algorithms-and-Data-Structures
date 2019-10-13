'''
Для каждого упражнения написать программную реализацию.
Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию).
Каждую задачу необходимо сохранять в отдельный файл.
Рекомендуем использовать английские имена, например, les_5_task_1, les_5_task_2, и т.д.
Для оценки «Отлично» необходимо выполнить оба задания.
Задача считается решённой, если в ней использована как минимум одна коллекция из модуля collections.
'''
'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре
квартала для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''
from collections import ChainMap

# Заполняем словари
# Для тестового ввода можно закомментировать этот блок
while True:
    try:
        count = int(input('Введите количество предприятий: '))
    except:
        print('Ошибка ввода!')
        continue
    company_map = ChainMap()
    for i in range(count):
        name = input('Введите название предприятия: ')
        while True:
            try:
                profit = int(input('Введите значение прибыли: '))
            except:
                print('Ошибка ввода!')
                continue
            break
        company_map = company_map.new_child({'name': name, 'profit': profit})
    break

# Оставил для теста
# result = 0
# company_1 = {'name' :  'A', 'profit' :900}
# company_2 = {'name' :  'B', 'profit' :1000}
# company_3 = {'name' :  'C', 'profit' :1100}
# company_4 = {'name' :  'D', 'profit' :1200}
# company_5 = {'name' :  'E', 'profit' :1500}
#
# company_map = ChainMap(company_1,company_2,company_3,company_4,company_5)
# count = 5

if count > 0:
    # Убираем пустой словарь и меняем порядок элементов
    # При тестовом вводе эти две строки нужно закомментировать
    company_map.maps.pop()
    company_map.maps.reverse()

    result = 0
    above = []
    below = []

    for c in company_map.maps:
        result += c['profit']
    print(f'Общая прибыль: {result}')
    avr = result / len(company_map.maps)
    print(f'Средняя прибыль:{avr}')
    for c in company_map.maps:
        if c['profit'] > avr:
            above.append(c["name"])
        if c['profit'] < avr:
            below.append(c["name"])
    print('Выше среднего:')
    for name in above:
        print(name, end=' ')
    print()
    print('Ниже среднего:')
    for name in below:
        print(name, end=' ')
