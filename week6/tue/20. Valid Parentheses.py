class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return False

        stack = []
        for c in s:

            if c in '[{(':
                stack.append(c)
            elif c in ')}]':
                if len(stack) == 0:
                    return False

                if c == '}' and stack[-1] == '{':

                    stack.pop()

                elif c == ']' and stack[-1] == '[':

                    stack.pop()
                elif c == ')' and stack[-1] == '(':

                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) != 0:
            return False
        else:
            return True
