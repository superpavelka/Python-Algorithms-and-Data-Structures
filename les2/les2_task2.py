'''
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''
while True:
    try:
        n = int(input('Введите число: '))
    except ValueError:
        print('Ошибка ввода!')
        continue
    even = 0
    odd = 0
    while True:
        remainder = n % 10
        if remainder % 2 == 0:
            even += 1
        else:
            odd += 1
        n = n // 10
        if n == 0:
            break
    print(f'Количество четных цифр: {even}')
    print(f'Количество нечетных цифр: {odd}')
    break
