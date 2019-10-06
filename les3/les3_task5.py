'''
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный»
 «максимальный отрицательный».
Это два абсолютно разных значения.
'''
import random

inf = float('inf')
max_neg_elem = -inf
max_neg_elem_i = -inf

while True:
    try:
        a_max_size = int(input('Введите количество элементов массива: '))
    except:
        print('Ошибка ввода!')
        continue
    print('Рандомный массив: ')
    a = [random.randint(-1000, 1000) for _ in range(0, a_max_size)]
    for item in a:
        print(f'{item:>5}',end ='')
    print()
    for item in range(0,a_max_size):
        print(f'{item:>5}',end ='')
    for i,elem in enumerate(a):
        if elem < 0 and elem > max_neg_elem:
            max_neg_elem = elem
            max_neg_elem_i = i
    if max_neg_elem > -inf:
        print()
        print(f'Максимальный отрицательный элемент: {max_neg_elem}')
        print(f'Индекс максимального отрицательно элемента: {max_neg_elem_i}')
    break