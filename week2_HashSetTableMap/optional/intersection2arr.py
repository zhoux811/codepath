n1, n2 = [4, 9, 5], [9, 4, 9, 8, 4]  # [4,9] or [9,4]
n1, n2 = [1, 2, 2, 1], [2, 2]  # [2]


def inters(arr1, arr2):
    s1 = set()
    s2 = set()

    for e in arr1:
        if e not in s1:
            s1.add(e)
    for e in arr2:
        if e not in s2:
            s2.add(e)

    l = []
    for e in s1:
        if e in s2:
            l.append(e)

    return l


print(inters(n1, n2))
