'''
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:
>>> sieve(2)
3
>>> prime(4)
7
>>> sieve(5)
11
>>> prime(1)
2
Примечание по профилированию кода: для получения достоверных результатов при замере
времени необходимо исключить/заменить функции print() и input() в анализируемом коде.
С ними вы будете замерять время вывода данных в терминал и время, потраченное пользователем,
на ввод данных, а не быстродействие самого алгоритма.
'''
'''
Для проверки просто запустите файл.
http://denisx.ru/tech/prime-number/prime-numbers-list/ вот тут есть список простых чисел до 100 000 для проверки
Ниже представлены результаты профилирования
'''

from math import sqrt
import cProfile

def sieve(num):
    prime_count = 0
    k = 5
    while True:
        if (num > 0):
            sieve = [i for i in range(num*k)]
            sieve[1] = 0

            for i in range(2, num*k):
                if sieve[i] != 0:
                    j = i * 2
                    while j < num*k:
                        sieve[j] = 0
                        j += i

            for index,prime_number in enumerate(sieve):
                if prime_number != 0:
                    prime_count += 1
                if prime_count == num:
                    #print(prime_number)
                    return prime_number
            k += 5
            prime_count = 0
'''
При профилировании принты были закомментированы
'''
print('Sieve results:')
for j in range(1,5):
    for i in range (1,21):
        print(f'{sieve(i*j):>5}', end='')
    print()

# sieve(10)
# 1000 loops, best of 5: 30.7 usec per loop
# sieve(100)
# 1000 loops, best of 5: 1.17 msec per loop
# sieve(500)
# 1000 loops, best of 5: 6.55 msec per loop
# sieve(1000)
# 1000 loops, best of 5: 13.5 msec per loop
# sieve(2000)
# 1000 loops, best of 5: 27.8 msec per loop
# prime(3000)
# 1000 loops, best of 5: 42.6 msec per loop
# prime(5000)
# 1000 loops, best of 5: 73 msec per loop

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#cProfile.run('sieve(10)')
# 5 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les4_task2.py:4(sieve)
#cProfile.run('sieve(100)')
# 6 function calls in 0.001 seconds
# 1    0.001    0.001    0.001    0.001 les4_task2.py:4(sieve)
#cProfile.run('sieve(250)')
# 6 function calls in 0.003 seconds
# 1    0.003    0.003    0.003    0.003 les4_task2.py:4(sieve)
#cProfile.run('sieve(500)')
#6 function calls in 0.007 seconds
# 1    0.007    0.007    0.007    0.007 les4_task2.py:4(sieve)
#cProfile.run('sieve(1000)')
#6 function calls in 0.014 seconds
# 1    0.014    0.014    0.014    0.014 les4_task2.py:4(sieve)
#cProfile.run('sieve(2000)')
#6 function calls in 0.028 seconds
# 1    0.027    0.027    0.028    0.028 les4_task2.py:4(sieve)

def prime(n):
    num = 2
    prime_count = 0
    is_prime = True
    if n > 0:
        while True:
            for d in range(2, int(sqrt(num)) + 1):
                if num % d == 0:
                    is_prime = False
            if is_prime:
                prime_count += 1
            if n == prime_count:
                #print(num)
                return num
            num += 1
            is_prime = True
'''
При профилировании принты были закомментированы
'''
print('Prime results:')
for j in range(1,5):
    for i in range (1,21):
        print(f'{prime(i*j):>5}', end='')
    print()
# prime(10)
# 1000 loops, best of 5: 29.2 usec per loop
# prime(100)
# 1000 loops, best of 5: 1.13 msec per loop
# prime(250)
# 1000 loops, best of 5: 4.66 msec per loop
# prime(500)
# 1000 loops, best of 5: 15.2 msec per loop
# prime(1000)
# 1000 loops, best of 5: 50.7 msec per loop
# prime(2000)
# 1000 loops, best of 5: 153 msec per loop

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#cProfile.run('prime(10)')
# 32 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les4_task2.py:25(prime)
#cProfile.run('prime(100)')
# 544 function calls in 0.002 seconds
# 1    0.001    0.001    0.001    0.001 les4_task2.py:25(prime)
#cProfile.run('prime(250)')
# 1586 function calls in 0.013 seconds
# 1    0.009    0.009    0.010    0.010 les4_task2.py:25(prime)
#cProfile.run('prime(500)')
# 3574 function calls in 0.024 seconds
# 1    0.023    0.023    0.024    0.024 les4_task2.py:25(prime)

