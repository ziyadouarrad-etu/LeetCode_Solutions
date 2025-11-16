class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max=0
        f=1
        for k in range(1,len(s)+1):
            for i in range(len(s)-k+1):
                f=1
                temp=set()
                for j in range(i, i+k):
                    if s[j] not in temp:
                        temp.add(s[j])
                    else:
                        f=0
                if f:
                    max=k
                    break
            if not f:
                break
        return max


        