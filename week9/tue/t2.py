message = list("hello world")
message = list("hello world hi word")

a = [1, 2, 3, 4]
a[2:4] = a[2:4][::-1]
print(a)


def reverseWords(arr):
    print(''.join(arr))
    slow = 0
    fast = 0
    while fast < len(arr) and slow < len(arr):
        if arr[fast] == " ":
            arr[slow:fast] = arr[slow:fast][::-1]
            slow = fast + 1
            fast += 1
        elif fast == len(arr) - 1:
            arr[slow:fast + 1] = arr[slow:fast + 1][::-1]
            slow = fast + 1
            fast += 1
        else:
            fast += 1
    arr.reverse()


reverseWords(message)
print(''.join(message))
