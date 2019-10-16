'''
Для оценки «Отлично» необходимо выполнить все требования, указанные в задании и примечаниях.

1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);

проанализировать 3 варианта и выбрать оптимальный;
c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев
в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.
Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
а проявили творчество, фантазию и создали универсальный код для замера памяти.
'''
import random
import sys


# Меняем исходную функцию так, чтобы она только печатала размер всего элемента
# без рекурсивного прохода внутрь и возвращала этот размер.
# Специально оставил закомментированную часть чтобы показать изменения исходной функции
def show_size(x, level=0):
    print('\t' * level, f'type =  {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')
    return sys.getsizeof(x)
    # if hasattr(x, '__iter__'):
    #     if hasattr(x, 'items'):
    #         for xx in x.items():
    #             show_size(xx, level + 1)
    #     elif not isinstance(x ,str):
    #         for xx in x:
    #             show_size(xx, level + 1)


# Аккумулиурует size и выводит на экран
def show_elements_size(*args):
    size = 0
    print('*' * 50)
    print('Elements: ')
    print('*' * 50)
    for arg in args:
        size += show_size(arg)
    print('*' * 50)
    print(f'Total size: {size} bytes')
    print('*' * 50)


# Вычисление максимального элемента из всех отрицательных через один список без использования встроенных функций
def max_neg1(a_max_size):
    inf = float('inf')
    max_neg_elem = -inf
    max_neg_elem_i = -inf

    a = [random.randint(-1000, 1000) for _ in range(0, a_max_size)]
    print('+' * 12)
    print('+ max_neg1 +')
    print('+' * 12)
    print('Array: ')
    for item in a:
        print(f'{item:>5}', end='')
    print()
    for i in range(0, a_max_size):
        print(f'{i:>5}', end='')
    for i, elem in enumerate(a):
        if elem < 0 and elem > max_neg_elem:
            max_neg_elem = elem
            max_neg_elem_i = i
    if max_neg_elem > -inf:
        print()
        print('Max negative element index:')
        print(max_neg_elem_i)
        print('Max negative element:')
        print(max_neg_elem)
        show_elements_size(inf, max_neg_elem, max_neg_elem_i, a, a_max_size)
        return (max_neg_elem_i, max_neg_elem)


# Вычисление максимального элемента из всех отрицательных через один словарь без использования встроенных функций
def max_neg2(a_max_size):
    inf = float('inf')
    max_neg_elem = -inf
    max_neg_elem_i = -inf
    print('+' * 12)
    print('+ max_neg2 +')
    print('+' * 12)
    print('Array: ')
    a = {i: random.randint(-1000, 1000) for i in range(0, a_max_size)}
    for item in a.values():
        print(f'{item:>5}', end='')
    print()
    for i in range(0, a_max_size):
        print(f'{i:>5}', end='')
    for i, elem in a.items():
        if elem < 0 and elem > max_neg_elem:
            max_neg_elem = elem
            max_neg_elem_i = i
    if max_neg_elem > -inf:
        print()
        print('Max negative element index:')
        print(max_neg_elem_i)
        print('Max negative element:')
        print(max_neg_elem)
        show_elements_size(inf, max_neg_elem, max_neg_elem_i, a, a_max_size)
        return (max_neg_elem_i, max_neg_elem)


# Вычисление максимального элемента из всех отрицательных через два списка с использованием встроенной функции max()
def max_neg3(a_max_size):
    a = [random.randint(-1000, 1000) for i in range(0, a_max_size)]
    print('+' * 12)
    print('+ max_neg3 +')
    print('+' * 12)
    print('Array: ')
    for item in a:
        print(f'{item:>5}', end='')
    print()
    for i in range(0, a_max_size):
        print(f'{i:>5}', end='')
    b = [value for value in a if value < 0]

    if len(b) > 0:
        max_neg_elem = max(b)
        for i, elem in enumerate(a):
            if elem == max_neg_elem:
                max_neg_elem_i = i
        if a_max_size > 0:
            print()
            print('Max negative element index:')
            print(max_neg_elem_i)
            print('Max negative element:')
            print(max_neg_elem)
            show_elements_size(max_neg_elem, max_neg_elem_i, a, b, a_max_size)
            return (max_neg_elem_i, max_neg_elem)
    else:
        return None

# Вычисление максимального элемента из всех отрицательных через два списка с использованием рекурсивной функции
def max2(L):
    if len(L)==1:
        return L[0]
    mid = (len(L))//2
    left_L = [L[i] for i in range(0, mid)]
    right_L = [L[i] for i in range(mid, len(L))]
    a = max2(left_L)
    b = max2(right_L)
    #show_elements_size(L, mid, left_L, right_L, a,b)
    return max(a,b)

def main_max(a_max_size):
    a = [random.randint(-1000, 1000) for i in range(0, a_max_size)]
    print('+' * 12)
    print('+ main_max +')
    print('+' * 12)
    print('Array: ')
    for item in a:
        print(f'{item:>5}', end='')
    print()
    for i in range(0, a_max_size):
        print(f'{i:>5}', end='')
    b = [value for value in a if value < 0]

    if len(b) > 0:
        max_neg_elem = max2(b)
        for i,elem in enumerate(a):
            if elem == max_neg_elem:
                max_neg_elem_i = i
                print()
                print('Index:')
                print(max_neg_elem_i)
                print('Max negative element:')
                print(max_neg_elem)
                show_elements_size(max_neg_elem, max_neg_elem_i, a, b, a_max_size)
        return (max_neg_elem_i, max_neg_elem)

if __name__ == "__main__":
    max_neg1(100)
    max_neg2(100)
    max_neg3(100)
    main_max(100)
