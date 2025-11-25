class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=1
        j=0
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                n+=1
            else:
                n=1
            if n<=2:
                j+=1
                nums[j]=nums[i]
        return j+1

        