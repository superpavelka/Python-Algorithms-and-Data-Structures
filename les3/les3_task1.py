'''
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''
import random

out_lst = []
out_lst_lst = []
a = [i for i in range(2, 100)]

for n in range(2, 10):
    for a_i in a:
        if a_i % n == 0:
            out_lst.append(a_i)
    print(f'Делитель {n} : Количество: {len(out_lst)} Элементы: {out_lst}')
    out_lst_lst.append(out_lst.copy())
    out_lst.clear()
