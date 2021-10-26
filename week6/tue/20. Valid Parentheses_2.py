class Solution:
    def isValid(self, s: str) -> bool:
        d = dict(zip(']})', '[{('))
        if not s:
            return False

        stack = []
        for c in s:

            if c in '[{(':
                stack.append(c)
            elif c in ')}]':
                if len(stack) != 0 and d[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) != 0:
            return False
        else:
            return True