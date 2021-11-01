from math import log10

# print(ord('0'))
# print(ord('1'))
# print(ord('9'))
#
# print(chr(48))
# print(chr(49))

nums = [
    1234,
    -234,
    +100,
    901,
    10,
    -234,
    -0]


def int2str(n):
    s = ''
    if n < 0:
        s += '-'
        n = -n

    if n == 0:
        return '0'

    d = int(log10(n))

    for i in range(d, -1, -1):
        # print(i)
        s += chr(
            n // (10 ** i) % 10
            + 48
        )
    return s


for nn in nums:
    print(int2str(nn))
