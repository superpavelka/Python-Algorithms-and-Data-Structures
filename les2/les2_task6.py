'''
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше
введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ.
'''
from random import randint

n = randint(0, 100)
try_ = 0
max_try = 10
print('Загадано число от 0 до 100.')
while True:
        try:
            n_try = int(input('Введите число: '))
        except ValueError:
            print('Ошибка ввода!')
            continue
        if n_try == n:
            print('Вы угадали число!')
            break
        elif n_try < n:
            print('Введенное вами число меньше загаданного!')
            print(f'Попыток осталось: {max_try - try_ - 1}')
        elif n_try > n:
            print('Введенное вами число больше загаданного!')
            print(f'Попыток осталось: {max_try - try_ - 1}')
        try_ += 1
        if (try_ == 10):
            print('Закончились попытки!')
            break
