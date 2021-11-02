class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # for i in range(len(digits),-1,-1):

        pos = len(digits) - 1

        while pos >= 0:

            if digits[pos] == 9:
                digits[pos] = 0
                pos -= 1

            else:

                digits[pos] += 1
                break

        if digits[0] == 0:
            digits.insert(0, 1)

        return digits