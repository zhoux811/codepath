def mult_o_3_5(n):
    return 3 * (
        sum(range(0, (n - 1) // 3 + 1, 1))
    ) + 5 * (
               sum(range(0, (n - 1) // 5 + 1, 1))
           ) - 15 * (
               sum(range(0, (n - 1) // 15 + 1, 1))
           )


# print(10 // 15)
# print(list(range(0, (10 - 1) // 3+1, 1)))
# print(list(range(0, (10 - 1) // 5+1, 1)))

print(mult_o_3_5(10))
print(mult_o_3_5(1000))

r = 0
for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        r += i
print(r)
