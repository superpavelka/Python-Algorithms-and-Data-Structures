'''7. Определить, является ли год, который ввел пользователь, високосным или не високосным.'''

correct_input = False
while not correct_input:
    try:
        y = int(input('Введите год: '))
    except ValueError:
        print('Ошибка ввода!')
        continue
    if y < 0:
        print('Значение года не может быть отрицательным!')
    else:
        correct_input = True

if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    print(f"{y} - обычный год")
else:
    print(f"{y} - високосный год")