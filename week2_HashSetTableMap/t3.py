print(sorted([1, 9, 3, 10, 11, 12, 4, 20, 13, 11, 11, 2]))

# [1, 2, 3, 4, 9, 10, 11, 11, 11, 12, 13, 20]

l = [0, 1, 1, 1, 1, 2]
i = 0
while i != len(l):
    print(len(l))
    if l[i] + 1 == l[i + 1]:
        l.pop(i)
    i += 1
    print(l)
