class Solution:
    def reverse(self, x: int) -> int:
        signe=-1 if x<0 else 1
        result = int(str(abs(x))[::-1])*signe
        result = result if -2**31< result < 2**31-1 else 0
        return result
        