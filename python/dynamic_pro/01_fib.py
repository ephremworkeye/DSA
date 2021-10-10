# time complexity o(2^n)
# space complexity = o(n)

# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(1))
# print(fib(3))
# print(fib(4))
# print(fib(40))


# to improve in dynmaic programming(memoization)

# def fib(n, d={}):
#     if n in d: return d[n]
#     if n <= 2: return 1
#     d[n] = fib(n-1, d) + fib(n-2, d)
#     return d[n]

# print(fib(1))
# print(fib(3))
# print(fib(4))
# print(fib(40))

# time complexity o(n)
# space complexity = o(n)

# or we can use the lru_cache from functools

from functools import lru_cache

@lru_cache
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(1))
print(fib(3))
print(fib(4))
print(fib(40))