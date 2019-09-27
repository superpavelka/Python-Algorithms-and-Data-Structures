'''
3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
'''
from random import random

correct_input = False
print('Введите границы для генерации целого числа:')
while not correct_input:
    try:
        m1 = int(input('Левая граница: '))
        m2 = int(input('Правая граница: '))
        correct_input = True
        if (m1 > m2):
            correct_input = False
            print('Ошибка ввода!Левая граница больше правой!')
    except ValueError:
        print('Ошибка ввода!')

n = int(random() * (m2 - m1 + 1)) + m1
print(n)

correct_input = False
print('Введите границы для генерации числа c плавающей точкой:')
while not correct_input:
    try:
        m1 = float(input('Левая граница: '))
        m2 = float(input('Правая граница: '))
        correct_input = True
        if (m1 > m2):
            correct_input = False
            print('Ошибка ввода!Левая граница больше правой!')
    except ValueError:
        print('Ошибка ввода!')

n = random() * (m2 - m1) + m1
print(round(n, 3))

correct_input = False
print('Введите границы для генерации символа:')
while not correct_input:
    m1 = ord(input('Левая граница: '))
    m2 = ord(input('Правая граница: '))
    correct_input = True
    if (m1 > m2):
        correct_input = False
        print('Ошибка ввода!Левая граница больше правой!')
n = int(random() * (m2 - m1 + 1)) + m1
print(chr(n))
