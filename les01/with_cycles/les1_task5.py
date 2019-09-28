'''
5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
'''
correct_input = False
print('Скрипт подразумевает использование символов только английского алфавита')
while not correct_input:
    try:
        n = int(input('Введите номер буквы: '))
        n += 96
    except ValueError:
        print('Ошибка ввода!')
        continue
    if n > 96 and n < 123:
        correct_input = True
    else:
        print('Ошибка ввода!')
print(chr(n))
