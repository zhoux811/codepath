arr = [1, 2, 3, 4, 5]

n = 5
i, temp = 1, 1
prod = [1 for i in range(n)]

for i in range(n):
    prod[i] = temp
    temp *= arr[i]

print(prod)


temp = 1

for i in range(n-1,-1,-1):
    prod[i] *=temp
    temp *= arr[i]

print(prod)