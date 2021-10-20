arr = [1, 2, 3, 4]


def map_f(n):
    return n + 1


def filter_f(n):
    return n - 1


def filter_f2(n):
    return True if n == 3 else False


def reduce_f(x, y):
    return x * y


m = list(map(map_f, arr))
f = list(filter(filter_f, arr))
f2 = list(filter(filter_f2, arr))

from functools import reduce

# r = reduce((lambda x, y: x * y), [1, 2, 3, 4])
r = reduce(reduce_f, [1, 2, 3, 4])

print(m)
print(f)
print(f2)
print(r)

"""
ld=lambda x, y: x * y
print(ld(1,2))
"""
