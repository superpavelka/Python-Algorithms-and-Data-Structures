'''
1.2 Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
'''
num = 5
result1 = 5 >> 2
result2 = result1 << 2
print(f'{num} >> 2 = {result1}')
print(f'{result1} << 2 = {result2}')
