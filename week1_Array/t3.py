def implode(n2):
    total = 0
    while n2 != 0:
        total += (n2 % 10) * (n2 % 10)
        n2 //= 10
    return total


n = 1001

print(implode(n))
seen = {54}

while implode(n) not in seen:

    if implode(n) == 1:
        print(5)
    else:
        seen.add(implode(n))
        n = implode(n)