'''
arr = [1, 2]

while len(arr) < 10:
    arr.append(arr[-1] + arr[-2])
print(arr)
'''

arr = [1, 2]
four_million = 4000000

while arr[-1] < four_million:
    arr.append(arr[-1] + arr[-2])
print(arr)
arr.pop()
print(arr)

test = [1, 2]
while test[-1] < 100:
    test.append(test[-1] + test[-2])
print(test)
test.pop()
print(test)
print(test[1::3])
print(sum(test[1::3]))


print(sum(arr[1::3]))
