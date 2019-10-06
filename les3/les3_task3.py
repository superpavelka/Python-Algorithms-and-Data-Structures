'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random

inf = float('inf')
max_elem = -inf
max_i = inf
min_elem = inf
min_i = inf

while True:
    try:
        a_max_size = int(input('Введите количество элементов массива: '))
    except:
        print('Ошибка ввода!')
        continue
    print('Рандомный массив: ')
    a = [random.randint(1, 100) for _ in range(0, a_max_size)]
    print(a)
    for i, elem in enumerate(a):
        if elem > max_elem:
            max_elem = elem
            max_i = i
        if elem < min_elem:
            min_elem = elem
            min_i = i
    print(f'Минимальный элемент: {min_elem}')
    print(f'Позиция минимального элемента: {min_i}')
    print(f'Максимальный элемент: {max_elem}')
    print(f'Позиция максимального элемента: {max_i}')
    a[max_i] = min_elem
    a[min_i] = max_elem
    print('Поменяли элементы и печатаем новый массив:')
    print(a)
    break
