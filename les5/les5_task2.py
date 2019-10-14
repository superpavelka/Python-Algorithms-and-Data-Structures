'''
Для каждого упражнения написать программную реализацию.
Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию).
Каждую задачу необходимо сохранять в отдельный файл.
Рекомендуем использовать английские имена, например, les_5_task_1, les_5_task_2, и т.д.
Для оценки «Отлично» необходимо выполнить оба задания.
Задача считается решённой, если в ней использована как минимум одна коллекция из модуля collections.
'''
'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, 
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. 
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной 
задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
'''
from collections import deque


def dec_to_hex(dec, list_of_numbers):
    hex = []
    while True:
        if dec >= 16:
            rem = dec % 16
            if rem > 9:
                rem = list_of_numbers[rem]
            hex.append(rem)
            dec = dec // 16
        elif dec != 0:
            if dec > 9:
                dec = list_of_numbers[dec]
            hex.append(dec)
            hex.reverse()
            return hex


def hex_to_dec(hex, list_of_numbers):
    hex_deq = deque(hex)
    dec = 0
    i = 0;
    while len(hex_deq):
        dec += list_of_numbers.index(hex_deq.pop()) * (16 ** i)
        i += 1
    return dec


list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
result = []
while True:
    try:
        num1 = list(input('Введите число 1: ').upper())
        for i, digit in enumerate(num1):
            if digit not in list_of_numbers:
                raise TypeError
        num2 = list(input('Введите число 2: ').upper())
        for i, digit in enumerate(num2):
            if digit not in list_of_numbers:
                raise TypeError
        break
    except TypeError:
        print('Ошибка ввода!')
print('Число 1: ')
print(num1)
print('Число 2: ')
print(num2)

mul_dec = hex_to_dec(num1, list_of_numbers) * hex_to_dec(num2, list_of_numbers)
sum_dec = hex_to_dec(num1, list_of_numbers) + hex_to_dec(num2, list_of_numbers)

mul_hex = dec_to_hex(mul_dec, list_of_numbers)
sum_hex = dec_to_hex(sum_dec, list_of_numbers)

print('Произведение: ')
print(mul_hex)
print('Сумма: ')
print(sum_hex)
