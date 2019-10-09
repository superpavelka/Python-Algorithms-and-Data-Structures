'''
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом
(не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
'''
'''
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный»
 «максимальный отрицательный».
Это два абсолютно разных значения.
'''
import random
import cProfile

# Вычисление максимального элемента из всех отрицательных через один список без использования встроенных функций
def max_neg1(a_max_size):
    inf = float('inf')
    max_neg_elem = -inf
    max_neg_elem_i = -inf

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

#max_neg1(10)
#1000 loops, best of 5: 355 usec per loop
#max_neg1(100)
#1000 loops, best of 5: 911 usec per loop
#max_neg1(500)
#1000 loops, best of 5: 3.84 msec per loop
#max_neg1(1000)
#1000 loops, best of 5: 7.37 msec per loop

#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#cProfile.run('max_neg1(10)')
#80 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les4_task1.py:22(max_neg1)
#cProfile.run('max_neg1(100)')
#711 function calls in 0.001 seconds
# 1    0.000    0.000    0.001    0.001 les4_task1.py:22(max_neg1)
#cProfile.run('max_neg1(500)')
#3524 function calls in 0.007 seconds
# 1    0.001    0.001    0.007    0.007 les4_task1.py:22(max_neg1)
#cProfile.run('max_neg1(1000)')
#7034 function calls in 0.014 seconds
# 1    0.002    0.002    0.014    0.014 les4_task1.py:22(max_neg1)

# Вычисление максимального элемента из всех отрицательных через один словарь без использования встроенных функций
def max_neg2(a_max_size):
    inf = float('inf')
    max_neg_elem = -inf
    max_neg_elem_i = -inf

    print('Рандомный массив: ')
    a = {i :random.randint(-1000, 1000) for i in range(0, a_max_size)}
    for item in a.values():
        print(f'{item:>5}',end ='')
    print()
    for item in range(0,a_max_size):
        print(f'{item:>5}',end ='')
    for i,elem in a.items():
        if elem < 0 and elem > max_neg_elem:
            max_neg_elem = elem
            max_neg_elem_i = i
    if max_neg_elem > -inf:
        print()
        print(f'Максимальный отрицательный элемент: {max_neg_elem}')
        print(f'Индекс максимального отрицательно элемента: {max_neg_elem_i}')

#max_neg2(10)
#1000 loops, best of 5: 278 usec per loop
#max_neg2(100)
#1000 loops, best of 5: 923 usec per loop
#max_neg1(500)
#1000 loops, best of 5: 3.86 msec per loop
#max_neg2(1000)
#1000 loops, best of 5: 7.43 msec per loop

#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#cProfile.run('max_neg2(10)')
#82 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les4_task1.py:22(max_neg2)
#cProfile.run('max_neg2(100)')
#715 function calls in 0.002 seconds
# 1    0.000    0.000    0.002    0.002 les4_task1.py:66(max_neg2)
#cProfile.run('max_neg2(500)')
#3522 function calls in 0.007 seconds
# 1    0.001    0.001    0.007    0.007 les4_task1.py:66(max_neg2)
#cProfile.run('max_neg2(1000)')
#7049 function calls in 0.014 seconds
# 1    0.002    0.002    0.014    0.014 les4_task1.py:66(max_neg2)

# Вычисление максимального элемента из всех отрицательных через два списка с использованием встроенной функции max()
def max_neg3(a_max_size):
    print('Рандомный массив: ')
    a = [random.randint(-1000, 1000) for i in range(0, a_max_size)]
    b = [value for value in a if value < 0]
    for item in a:
        print(f'{item:>5}',end ='')
    print()
    for item in range(0,a_max_size):
        print(f'{item:>5}',end ='')
    if len(b) > 0:
        max_neg_elem = max(b)
        for i,elem in enumerate(a):
            if elem == max_neg_elem:
                max_neg_elem_i = i
        if a_max_size > 0:
            print()
            print(f'Максимальный отрицательный элемент: {max_neg_elem}')
            print(f'Индекс максимального отрицательно элемента: {max_neg_elem_i}')
    else:
        print(f'Случайный массив не содержит отрицательных элементов!')

#max_neg3(10)
#1000 loops, best of 5: 279 usec per loop
#max_neg3(100)
#1000 loops, best of 5: 922 usec per loop
#max_neg3(500)
#1000 loops, best of 5: 3.87 msec per loop
#max_neg3(1000)
#1000 loops, best of 5: 7.51 msec per loop

#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#cProfile.run('max_neg3(10)')
#84 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les4_task1.py:110(max_neg3)
#cProfile.run('max_neg3(100)')
#714 function calls in 0.002 seconds
# 1    0.000    0.000    0.002    0.002 les4_task1.py:110(max_neg3)
#cProfile.run('max_neg3(500)')
#3529 function calls in 0.007 seconds
# 1    0.001    0.001    0.007    0.007 les4_task1.py:110(max_neg3)
#cProfile.run('max_neg3(1000)')
#7036 function calls in 0.014 seconds
# 1    0.002    0.002    0.014    0.014 les4_task1.py:110(max_neg3)

# Вычисление максимального элемента из всех отрицательных через два списка с использованием рекурсивной функции
def max2(L):
    if len(L)==1:
        return L[0]
    mid = (len(L))//2
    left_L = [L[i] for i in range(0, mid)]
    right_L = [L[i] for i in range(mid, len(L))]
    a = max2(left_L)
    b = max2(right_L)
    return max(a,b)

def main(a_max_size):
    print('Рандомный массив: ')
    a = [random.randint(-1000, 1000) for i in range(0, a_max_size)]
    b = [value for value in a if value < 0]
    for item in a:
        print(f'{item:>5}', end='')
    print()
    for item in range(0, a_max_size):
        print(f'{item:>5}', end='')
    if len(b) > 0:
        max_neg_elem = max2(b)
        for i,elem in enumerate(a):
            if elem == max_neg_elem:
                max_neg_elem_i = i
        print()
        print(f'Максимальный отрицательный элемент: {max_neg_elem}')
        print(f'Индекс максимального отрицательно элемента: {max_neg_elem_i}')

#main(10)
#1000 loops, best of 5: 303 usec per loop
#main(100)
#1000 loops, best of 5: 1.17 msec per loop
#main(500)
#1000 loops, best of 5: 4.97 msec per loop
#main(1000)
#1000 loops, best of 5: 9.75 msec per loop

#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#cProfile.run('main(10)')
# 102 function calls (98 primitive calls) in 0.000 seconds
# 5/1    0.000    0.000    0.000    0.000 les4_task1.py:157(max2)
#cProfile.run('main(100)')
#1186 function calls (1082 primitive calls) in 0.002 seconds
# 105/1    0.000    0.000    0.000    0.000 les4_task1.py:157(max2)
#cProfile.run('main(500)')
#5646 function calls (5174 primitive calls) in 0.009 seconds
# 473/1    0.001    0.000    0.001    0.001 les4_task1.py:157(max2)
#cProfile.run('main(1000)')
#11511 function calls (10517 primitive calls) in 0.017 seconds
# 995/1    0.002    0.000    0.003    0.003 les4_task1.py:157(max2)

'''Можно сделать вывод, что функция работает одинаково через список и через словарь, такие же результаты
функция показала при нахождении максимума через встроенную функцию. Рукурсивный вариант выполняется дольше.'''