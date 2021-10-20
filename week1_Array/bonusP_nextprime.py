import math

test_cases = [

    3, -2, -5678, 3, 1,

]


def check_prime(n):
    if n == 1:
        return False
    for i in range(2, 1 + int(math.sqrt(n))):
        if n % i == 0:
            return False
    ##print(n)
    return True


arr = list(range(1, 100))

print(list(filter(check_prime, arr)))


def next_prime(n):
    n += 1
    while not check_prime(n):
        n += 1
    return n


print(
[next_prime(k) for k in list(filter(check_prime, arr))]
)
