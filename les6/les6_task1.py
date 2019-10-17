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
import platform

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
        show_elements_size(inf, max_neg_elem, max_neg_elem_i, a, a_max_size, item, i, elem)
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
        show_elements_size(inf, max_neg_elem, max_neg_elem_i, a, a_max_size, item, i, elem)
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
            show_elements_size(max_neg_elem, max_neg_elem_i, a, b, a_max_size,item,i,elem)
            return (max_neg_elem_i, max_neg_elem)
    else:
        return None

if __name__ == "__main__":
    print(sys.version)
    print(sys.platform)
    print(platform.architecture())
    max_neg1(100)
    max_neg2(100)
    max_neg3(100)

'''
3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)]
win32
('32bit', 'WindowsPE')
Из результатов выполнения видно, что лучшей реализацией с точки зрения используемой статической памяти 
является функция max_neg1 - Total size: 560 bytes. Следующая функция max_neg2 сильно проигрывает по памяти 
(Total size: 2720 bytes) т.к. в ее реализации используется словарь вместо списка, который сам по себе 
занимает 2620 bytes вместо 460 bytes на список из первой реализации. Третья реализация max_neg3 хуже чем
max_neg1 но лучше чем max_neg2 т.к. использует два списка 460 bytes  и 268 bytes соответственно и в общем
она использует 812 bytes памяти. Также можно обратить внимание, что переменные-счетчики цикла также 
используют память и хранят последнее значение даже после выхода из цикла вплоть до завершения работы скрипта,
поэтому их количество также влияет на используемую память.
'''