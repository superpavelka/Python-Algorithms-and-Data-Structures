'''8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).'''

correct_input = False
while not correct_input:
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        c = int(input('Введите третье число: '))
        correct_input = True
    except ValueError:
        print('Ошибка ввода!')

if a == b and b == c:
    print('Все числа равны!')
elif a == b:
    print('Первое число равно второму числу, среднего нет!')
elif b == c:
    print('Второе число равно третьему числу, среднего нет!')
elif a == c:
    print('Первое число равно третьему числу, среднего нет!')
elif (a < b and a > c) or (a < c and a > b):
    print(f'Число {a} является средним')
elif (b < a and b > c) or (b < c and b > a):
    print(f'Число {b} является средним')
elif (c < a and c > b) or (c < b and c > a):
    print(f'Число {c} является средним')