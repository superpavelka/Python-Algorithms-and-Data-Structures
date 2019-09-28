'''
1.1 Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
1.2 Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
'''
a = 5
b = 6
result = a & b
print(f'{a} & {b} = {result}')
result = a | b
print(f'{a} | {b} = {result}')
result = a ^ b
print(f'{a} ^ {b} = {result}')

result1 = a >> 2
result2 = result1 << 2
print(f'{a} >> 2 = {result1}')
print(f'{result1} << 2 = {result2}')
