class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        total=0
        l=len(s)
        roman={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000}
        while i<l:                
            current_val=roman[s[i]]
            if i<l-1:
                next_val=roman[s[i+1]]
                if current_val<next_val:
                    total+=(next_val-current_val)
                    i+=2
                    continue
            total+=current_val
            i+=1
            f=0
        return total