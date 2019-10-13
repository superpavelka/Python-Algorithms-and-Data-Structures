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
# num1 = list(input('Введите число: '))
# num2 = list(input('Введите число: '))
list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

while True:
    try:
        num1 = list(input('Введите число: ').upper())
        num2 = list(input('Введите число: ').upper())
        for i,digit in enumerate(num1):
            if digit not in list_of_numbers:
                raise TypeError
        for i,digit in enumerate(num2):
            if digit not in list_of_numbers:
                raise TypeError
        break
    except TypeError:
        print('Ошибка ввода!')

num1.reverse()
num2.reverse()
num1_dec = 0
num2_dec = 0
for i,digit in enumerate(num1):
    num1_dec += list_of_numbers.index(digit) * (16**i)
for i,digit in enumerate(num2):
    num2_dec += list_of_numbers.index(digit) * (16**i)

mul_dec = num1_dec * num2_dec
sum_dec = num1_dec + num2_dec

mul_hex = []

for i in str(mul_dec):
    if int(i) <= 16:
        rem = int(i) % 16
        if rem > 9:
            rem = list_of_numbers.index(rem)
        mul_hex.append(int(i) % 16)

print(mul_dec)
print(sum_dec)

