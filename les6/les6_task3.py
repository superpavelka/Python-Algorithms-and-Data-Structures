import memory_profiler
import random

# Вычисление максимального элемента из всех отрицательных через один словарь без использования встроенных функций
@profile
def max_neg3(a_max_size):
    a = [random.randint(-1000, 1000) for i in range(0, a_max_size)]
    b = [value for value in a if value < 0]

    if len(b) > 0:
        max_neg_elem = max(b)
        for i,elem in enumerate(a):
            if elem == max_neg_elem:
                max_neg_elem_i = i
        if a_max_size > 0:
            return (max_neg_elem_i, max_neg_elem)
    else:
        return None

if __name__ == "__main__":
    max_neg3(100)