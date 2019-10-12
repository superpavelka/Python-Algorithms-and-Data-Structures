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
                return num
            num += 1
            is_prime = True


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


'''
На графике видно что зависимость Sieve имеет небольшой загиб вверх и больше похожа на n logn
Зависимость Prime больше похожа на n2
'''