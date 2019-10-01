'''
2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
'''
correct_input = False
try:
    print('Введите координаты первой точки x1 и y1')
    x1 = int(input('x1= '))
    y1 = int(input('y1= '))
    print('Введите координаты второй точки x2 и y2')
    x2 = int(input('x2= '))
    y2 = int(input('y2= '))
    correct_input = True
except ValueError:
    print('Ошибка ввода!')
if (correct_input):
    if x1 != x2:
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1
        if k == 1 and b != 0:
            if b > 0:
                print(f'Уравнение линейной функции: y = x + {b}')
            else:
                print(f'Уравнение линейной функции: y = x - {-b}')
        elif k == 1 and b == 0:
            print(f'Уравнение линейной функции: y = x')
        elif k != 0 and b != 0:
            if b > 0:
                print(f'Уравнение линейной функции: y = {k}x + {b}')
            else:
                print(f'Уравнение линейной функции: y = {k}x - {-b}')
        elif k == 0 and b != 0:
            print(f'Уравнение линейной функции: y = {b}')
        elif k != 0 and b == 0:
            print(f'Уравнение линейной функции: y = {k}x')
    else:
        print(f'Уравнение линейной функции: x = {x1}')
