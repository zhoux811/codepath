# print(ord('0'))
# print(ord('1'))
# print(ord('9'))

s1 = '-001234'
s2 = '-234'
s3 = '+100'
s4 = '-000234'
s5 = '-0'


def str2int(s):
    ten = 0
    sum = 0
    for i in range(len(s) - 1, -1, -1):
        # print(i)
        if s[i] in '1234567890':
            sum += 10 ** ten * (ord(s[i]) - 48)
        elif s[i] == '-':
            sum *= -1
        elif s[i] == '+':
            pass
        else:
            print('bad interger syntax')
            pass
        ten += 1
    return sum


print(str2int(s1))
print(str2int(s2))
print(str2int(s3))
print(str2int(s4))
print(str2int(s5))
