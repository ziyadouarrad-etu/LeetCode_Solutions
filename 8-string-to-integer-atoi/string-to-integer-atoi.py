class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        signe = 1
        if s[0] == "-" or s[0] == "+":
            if s[0] == "-":
                signe = -1
            s = s[1:]

        result = 0
        for i in range(len(s)):
            if s[i].isdigit():
                result = result * 10 + int(s[i])
            else:
                break
            if result * signe > 2**31 - 1:
                result = 2**31 - 1
                break
            elif result * signe < -(2**31):
                result = 2**31
                break
        result = result * signe

        return result
