a, b = [1, 4, 6, 9], 10
a, b = [1, 5, 5, 9], 10


def first_2sum(nums, target):
    d = dict()
    L = len(nums)



    """
    for i in range(L):
        for j in range(i):
            if nums[i] + nums[j] == target and i != j:
                print([i, j], [nums[i], nums[j]])
                return [i, j]
    """

    """
    for i in range(L):
        if nums[i] not in d:
            d[target - nums[i]] = i
        else:
            print([i, d[nums[i]]], [nums[i], target - nums[i]])
            return [i, d[nums[i]]]
    """


first_2sum(a, b)
