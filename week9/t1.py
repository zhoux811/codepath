def getD(encoded: str):
    decoded = ''
    ptr = 0

    while ptr != len(encoded):

        if encoded[ptr].isalpha():
            decoded += encoded[ptr]
        elif encoded[ptr].isdigit():
            parenthsis_score = 1
            ptr += 2
            start = ptr
            while parenthsis_score != 0:
                print(encoded[ptr])
                if encoded[ptr] == '[':
                    parenthsis_score += 1
                elif encoded[ptr] == ']':
                    parenthsis_score -= 1
                ptr += 1

            decoded += int(encoded[ptr]) * getD(encoded[start+1:ptr-2])

    return decoded


print(getD('1[b]'))
