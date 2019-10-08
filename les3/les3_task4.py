'''
4. Определить, какое число в массиве встречается чаще всего.
'''
import random
numbers = []
most_common = []
max_most_common = 0
while True:
    try:
        a_max_size = int(input('Введите количество элементов массива: '))
    except:
        print('Ошибка ввода!')
        continue
    print('Рандомный массив: ')
    a = [random.randint(1, 5) for _ in range(0, a_max_size)]
    print(a)
    for a_i in a:
        if len(most_common) == 0:
            numbers.append(a_i)
            most_common.append(0)
        if a_i in numbers:
            i = numbers.index(a_i)
            most_common[i]+=1
        else:
            numbers.append(a_i)
            most_common.append(1)
    for i,number in enumerate(numbers):
        print(f'Число: {number} Количество повторов в массиве:  {most_common[i]}')
        if max_most_common < most_common[i]:
            max_most_common = most_common[i]
            max_freq_n = number
    print(f'Наиболее часто встречаемое число: {max_freq_n} Количество повторов: {max_most_common}')
    break