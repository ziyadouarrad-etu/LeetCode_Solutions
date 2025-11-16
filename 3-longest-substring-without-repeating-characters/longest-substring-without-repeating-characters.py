class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp=set()
        deb, fin = 0, 0
        max_len=0
        while fin<len(s):
            if s[fin] not in temp:
                temp.add(s[fin])
                fin+=1
            else:                
                temp.remove(s[deb])
                deb+=1
            max_len=max(max_len, fin-deb)

        return max_len
