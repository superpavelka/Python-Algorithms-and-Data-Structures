'''
1.1 Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
'''

correct_input = False

while not correct_input:
    try:
        print('Введите числа a и b')
        a = int(input('a= '))
        b = int(input('b= '))
    except ValueError:
        print('Ошибка ввода!')
        continue
    print('Введите символ операции')
    print('& -- AND')
    print('| -- OR')
    print('^ -- XOR')
    o = (input('operation= '))
    if o == '&':
        result = a & b
        correct_input = True
    elif o == '|':
        result = a | b
        correct_input = True
    elif o == '^':
        result = a ^ b
        correct_input = True
    else:
        print('Некорректный ввод операции!')
print(f'{a} {o} {b} = {result}')
