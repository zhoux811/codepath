s = [
    'III', 'IV', 'IX', 'LVIII', 'MCMXCIV'
]


def r2i(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if len(s) == 0:
        return 'wtf'
    elif len(s) == 1:
        return roman[s]
    else:
        ans = roman[s[-1]]
        for i in range(len(s) - 1, 0, -1):
            # print( s[i] )
            # print( roman[s[i]] )
            if roman[s[i-1]] >= roman[s[i]]:
                ans += roman[s[i-1]]
            elif roman[s[i-1]] < roman[s[i]]:
                ans -= roman[s[i-1]]
            else:
                print('error')

    return ans


for ss in s:
    print('\n')
    print(r2i(ss))
