# inplace

def reverseWords( s: str) -> str:
    s = s.strip()
    if s == '':
        return ''

    ns = ''

    left, right = len(s) - 1, len(s)
    while left != 0:

        if s[left] != ' ':
            left -= 1
        else:
            ns += s[left + 1:right].strip() + ' '

            while s[left] == ' ':
                left -= 1

            right = left + 1

    ns += s[left:right].strip()

    return ns


print(reverseWords( 'the sky is blue'))