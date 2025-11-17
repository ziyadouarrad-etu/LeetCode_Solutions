class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d={
            '{':'}',
            '[':']',
            '(':')'
        }
        t=[]
        for i in s:
            if i in d:
                t.append(i)
            else:
                if t and i==d[t[-1]]:
                    t.pop()
                else:
                    return False
        return len(t)==0




