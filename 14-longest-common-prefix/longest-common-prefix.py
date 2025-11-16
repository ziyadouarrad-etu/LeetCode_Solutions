class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i=0
        s=''
        while True:
            try:
                temp=list(set(string[i] for string in strs))
                if len(temp)>1:
                    break
                else:
                    i+=1
                    s+=temp[0]
            except:
                break
        return s


        