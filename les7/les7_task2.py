'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''
import random

def MergerSort(a):
    def MergerGroup(a, left, m, right):
        if left >= right: return None
        if m < left or right < m: return None
        t = left
        # подгруппа 2
        for j in range(m + 1, right + 1):
            # цикл подгруппы 1
            for i in range(t, j):
                if a[j] < a[i]:
                    r = a[j]
                    # итерационно переставляем элементы, чтобы упорядочить
                    for k in range(j, i, -1):
                        a[k] = a[k - 1]
                    a[i] = r
                    # проджолжение вставки в группе 1
                    t = i
                    # к следующему узлу из подгруппы 2
                    break

    if len(a) < 2: return None
    k = 1
    while k < len(a):
        g = 0
        while g < len(a):  # группы
            z = g + k + k - 1  # последний эл-т группы
            r = z if z < len(a) else len(a) - 1  # последняя группа
            MergerGroup(a, g, g + k - 1, r)  # слияние
            g += 2 * k
        k *= 2

if __name__ == "__main__":
    a_max_size = 10
    a = [random.uniform(0,50)  for _ in range(0, a_max_size)]
    print(a)
    MergerSort(a)
    print(a)