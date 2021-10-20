import math


def find_digits(num):
    digits = 0
    while num != 0:
        num //= 10
        digits += 1
    return digits


def implode(num):
    # digits = math.log(num, 10)
    # print(1 + int(digits))

    print(num)
    digits = []
    while num != 0:
        digits.insert(0, num % 10)
        num //= 10
    print(digits)

    print(sum([d * d for d in digits]))


implode(1111123)
# print(find_digits(987654321))
