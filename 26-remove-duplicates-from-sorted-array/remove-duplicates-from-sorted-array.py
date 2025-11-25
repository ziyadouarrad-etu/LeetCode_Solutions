class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while(i<len(nums)-1):
            n,m=nums[i],nums[i+1]
            if n!=m:
                i+=1
            else:
                nums.pop(i)
        return i+1