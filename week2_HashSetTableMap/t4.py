s = [1,2,3]

max_l, curr_l = 1, 1
for e in s:
    while (e + curr_l in s or e - curr_l in s):
        if e + curr_l in s and e - curr_l in s:
            curr_l += 2
        elif e + curr_l in s or e - curr_l in s:
            curr_l += 1
    max_l = max(max_l, curr_l)
    curr_l = 1
print(max_l)