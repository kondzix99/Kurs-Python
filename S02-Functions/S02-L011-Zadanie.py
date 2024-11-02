import time
import functools

@functools.lru_cache(maxsize=100)
def fib(n):
    if n < 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result

start = time.time()

for i in range(1,80):
    print("{} liczba to ciagu Fibonacciego to {}, a czas to {}".format(i, fib(i), time.time()-start))

stop = time.time()

print("Calkowity czas pomiaru to: ", stop-start)

print(fib.cache_info())