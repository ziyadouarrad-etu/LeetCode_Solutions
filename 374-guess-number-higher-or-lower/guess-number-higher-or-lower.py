# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        a = 1
        b = n
        while True:
            c = (a + b) // 2
            if guess(c) == 0:
                return c
            elif guess(c) == 1:
                a = c + 1
            else:
                b = c - 1
