import memory_profiler
import random

# Вычисление максимального элемента из всех отрицательных через один словарь без использования встроенных функций
@profile
def max_neg2(a_max_size):
    inf = float('inf')
    max_neg_elem = -inf
    max_neg_elem_i = -inf

    a = {i :random.randint(-1000, 1000) for i in range(0, a_max_size)}
    # for item in a:
    #     print(f'{item:>5}',end ='')
    for i,elem in a.items():
        if elem < 0 and elem > max_neg_elem:
            max_neg_elem = elem
            max_neg_elem_i = i
    if max_neg_elem > -inf:
        # print()
        # print('Index:')
        # print(max_neg_elem_i)
        # print('Max negative element:')
        # print(max_neg_elem)
        return (max_neg_elem_i, max_neg_elem)

if __name__ == "__main__":
    max_neg2(100)