#  meant to practice a few things, mainly a morning wakeup!

#standard recursive fibonacci equation
#       n is the number we are starting from
#              n should be > 0 and an int
def fibo(n):
    # check that n is an integer
    if type(n) != int:
        raise TypeError("n must be an integer")
    if n <= 0:
        raise TypeError("n must be greater than 0")

    # set up fibonacci first element
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fibo(n - 1) + fibo(n - 2)


# we will manually create a cache system here
# explicit memoization
fibonacci_cache = {}

def fibonacci_the_long_way(numba):
    #if n is in our cach call from cache
    if numba in fibonacci_cache:
        return fibonacci_cache[numba]

    # check that n is an integer
    if type(numba) != int:
        raise TypeError("n must be an integer")
    if numba <= 0:
        raise TypeError("n must be greater than 0")

    # set up fibonacci first element
    if numba == 1:
        value = 1
    if numba == 2:
        value = 1
    elif numba > 2:
        value = fibo(numba - 1) + fibo(numba - 2)

    fibonacci_cache[numba] = value
    return value

###  Get fancy using L1 cache, who is a sexy beast?  Why YOU are of course!
# implicit memoization
from functools import lru_cache
@lru_cache(maxsize = 1000)
def fibonacci(number):
    # check that n is an integer
    if type(number) != int:
        raise TypeError("n must be an integer")
    if number <= 0:
        raise TypeError("n must be greater than 0")

    # set up fibonacci first element
    if number == 1:
        return 1
    if number == 2:
        return 1
    if number > 2:
        return fibo(number - 1) + fibo(number - 2)


# This allows us to test 1-51 our curret algorithm
#      f is any function we have written
#               f should take in a single positive int value
def test_our_fibo_style(f):
    for x in range(1, 51):
        print(x, ' : ', f(x))


test_our_fibo_style(fibonacci_the_long_way)
