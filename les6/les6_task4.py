import memory_profiler
import random

# Вычисление максимального элемента из всех отрицательных через два списка с использованием рекурсивной функции
@profile
def max2(L):
    if len(L)==1:
        return L[0]
    mid = (len(L))//2
    left_L = [L[i] for i in range(0, mid)]
    right_L = [L[i] for i in range(mid, len(L))]
    a = max2(left_L)
    b = max2(right_L)
    return max(a,b)

@profile
def main(a_max_size):
    a = [random.randint(-1000, 1000) for i in range(0, a_max_size)]
    b = [value for value in a if value < 0]

    if len(b) > 0:
        max_neg_elem = max2(b)
        for i,elem in enumerate(a):
            if elem == max_neg_elem:
                max_neg_elem_i = i
        return (max_neg_elem_i, max_neg_elem)

if __name__ == "__main__":
    main(100)