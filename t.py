# class A:
#     def do_thing(self):
#         print('From A')

# class B(A):
#     def do_thing(self):
#         print('From B')

# class C(A):
#     def do_thing(self):
#         print('From C')

# class D(B, C):
#     pass

# d = D()
# d.do_thing()
# from concurrent.futures import ProcessPoolExecutor
# import time
#
#
# def t():
#     while True:
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     t()
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         executor.

import concurrent.futures
import math

PRIMES = [
    1,
    2,
    3,
    4,
    5,
    6
]

import time
def is_prime(n):
    while True:
        time.sleep(1)
        print(n)
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    main()
    a = 1
    a = 2
    a = 3
    a = 4
