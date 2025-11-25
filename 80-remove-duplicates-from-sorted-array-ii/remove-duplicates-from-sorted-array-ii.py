class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        i=0
        while i<len(nums):
            n=nums[i]
            d[n]=d.get(n,0)+1
            if d[n]>2:
                nums.pop(i)
            else:
                i+=1
        return i

        