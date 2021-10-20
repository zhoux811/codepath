"""
Input: [1, 9, 3, 10, 4, 20 , 2]
Output: 4
[1, 3, 4, 2] is the longest subsequence of consecutive elements.

Input: [36, 41, 56, 35, 44, 33, 34, 43, 92, 32, 42]
Output: 5
Note: [36, 35, 33, 34, 32] is the longest subsequence of consecutive elements.

Input: [2]
Output: 1

Input: []
Output: 0

Input: [3, 9, 50, 2, 8, 4, 1]
Output: 4
Note: [3, 2, 4, 1] is the longest subsequence of consecutive elements.

Input: [1, 5, 29, 4, 3, 2, 1]
Output: 5
Note: [1, 5, 4, 3, 2] is the longest subsequence of consecutive elements,
duplicates don't add to the count.
"""

Input = [
    [1, 5, 29, 4, 3, 2, 1],  # 5
    [1, 5, 29, 4, 3, 2, 1, 0],  # 6
    [3, 9, 50, 2, 8, 4, 1],  # 4
    [],  # 0
    [2],  # 1
    [36, 41, 56, 35, 44, 33, 34, 43, 92, 32, 42],  # 5
    [1, 9, 3, 10, 4, 20, 2],  # 4
    [1, 9, 3, 10, 11, 12, 4, 20, 13, 11, 11, 2]  # 5
]


def solution_sort(arr):
    if len(arr) == 0:
        return 0
    sorted_arr = sorted(arr)  # or we can sort the original.
    i = 0
    while i != len(sorted_arr) - 1:
        if sorted_arr[i] == sorted_arr[i + 1]:
            sorted_arr.pop(i + 1)
        else:
            i += 1
    i = 0
    max_length = 1
    curr_length = 1
    while i != len(sorted_arr) - 1:
        # print('curr: %d' , curr_length)
        # print('max: %d ', max_length)
        if sorted_arr[i] + 1 == sorted_arr[i + 1]:
            curr_length += 1
            i += 1
        else:
            max_length = max(max_length, curr_length)
            curr_length = 1
            i += 1
    max_length = max(max_length, curr_length)
    return max_length


def solution_2ptr(arr):
    if len(arr) == 0:
        return 0
    sorted_arr = sorted(arr)  # or we can sort the original.
    # print(sorted_arr)
    curr_length = 1
    max_length = 1
    for i in range(0, len(sorted_arr) - 1):
        if sorted_arr[i] + 1 == sorted_arr[i + 1]:
            curr_length += 1
        elif sorted_arr[i] == sorted_arr[i + 1]:
            i += 1
        else:
            i += 1
            curr_length = 1
        max_length = max(max_length, curr_length)
    return max_length


def solution_set1(arr):
    # print(arr)
    if len(arr) == 0:
        return 0
    s = set()
    for e in arr:
        if e not in s:
            s.add(e)

    l = list(s)
    # print(l)
    curr_l = 1
    max_l = 1
    for i in range(len(l) - 1):

        # print('curr: %d' , curr_l)
        # print('max: %d ', max_l)
        if l[i] + 1 == l[i + 1]:
            curr_l += 1
        else:
            max_l = max(curr_l, max_l)
            curr_l = 1
    return max(max_l, curr_l)


def solution_set2(arr):
    # print(arr)
    if len(arr) == 0:
        return 0
    s = set()
    for e in arr:
        if e not in s:
            s.add(e)
    longest = 1
    for i in range(len(arr)):
        if arr[i] - 1 in s:
            continue
        else:
            curr_n = arr[i]
            curr_l = 1
            while curr_n + 1 in s:
                curr_n = curr_n + 1
                curr_l += 1
            longest = max(longest, curr_l)
    return longest


for a in Input:
    print(solution_sort(a))
    print(solution_2ptr(a))
    print(solution_set1(a))
    print(solution_set2(a))
    print('\n')
