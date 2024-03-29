'''
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5, если индексация
начинается с нуля), т.к. именно в этих позициях первого массива стоят
четные числа.
'''
import random

even_i = []
while True:
    try:
        a_max_size = int(input('Введите количество элементов массива: '))
    except:
        print('Ошибка ввода!')
        continue
    print('Рандомный массив: ')
    a = [random.randint(1, 100) for _ in range(0, a_max_size)]
    print(a)
    for i,elem in enumerate(a):
        if elem % 2 == 0:
            even_i.append(i)
    print('Индексы четных элементов: ')
    print(even_i)
    break
