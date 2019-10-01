'''
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
'''
while True:
    try:
        n = int(input('Введите число: '))
    except ValueError:
        print('Ошибка ввода!')
        continue
    str_n = ''
    if n <0 :
        str_n += '-'
        n = n * (-1)
    while True:
        remainder = n % 10
        str_n += str(remainder)
        n = n // 10
        if n == 0:
            break
    print(f'Число наоборот: {str_n}')
    break
