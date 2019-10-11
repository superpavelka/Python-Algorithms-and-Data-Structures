from math import sqrt
import cProfile


def sieve(n):
    if (n > 1):
        sieve = [i for i in range(n)]
        sieve[1] = 0

        for i in range(2, n):
            if sieve[i] != 0:
                j = i * 2
                while j < n:
                    sieve[j] = 0
                    j += i

        result = [i for i in sieve if i != 0]
        print(result)
    else:
        print('Некорректный ввод')


# sieve(10)

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
