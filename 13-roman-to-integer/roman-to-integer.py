class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        total=0
        l=len(s)
        while i<l:
            if i<l-1:
                current_val=self.roman(s[i])
                next_val=self.roman(s[i+1])
                if current_val<next_val:
                    total+=(next_val-current_val)
                    i+=2
                    continue
            total+=self.roman(s[i])
            i+=1
            f=0
        return total
    
    def roman(self,s):
        roman_dict={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000}
        return roman_dict[s]