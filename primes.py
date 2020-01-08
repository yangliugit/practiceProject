# -*-coding: utf-8 -*-

#
# def _odd_iter():
#     n = 1
#     while True:
#         n += 2
#         yield n
#
#
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
#
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)
#
#
# for n in primes():
#     if n < 100:
#         print n
#     else:
#         break

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

def make_counter_test():
  mc = make_counter()
  print(mc())
  print(mc())
  print(mc())

make_counter_test()