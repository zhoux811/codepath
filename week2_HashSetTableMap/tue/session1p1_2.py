import collections


def fre_k(arr, k):
    s = collections.Counter(arr)
    for e in s:
        if s[e] == k:
            return e
    return None


def fre_k2(arr, k):
    s = collections.Counter(arr)

    return [e for e in s if s[e] == k]


def fre_k3(arr, k):
    s = collections.Counter(arr)

    def filter_f(e):
        if s[e] == k:
            return True

    return list(filter(filter_f, arr))


print(
    # fre_k([1, 2, 3], 3)
    # fre_k3([1, 2, 2, 1, 4, 5], 2)  # 1 or 2
    fre_k3([1, 2, 3, 2, 1, 2, 3, 2, 1], 2)
)
