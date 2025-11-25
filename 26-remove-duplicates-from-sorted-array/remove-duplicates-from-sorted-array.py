class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        s=set()
        while(i<len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
                i+=1
            else:
                nums.pop(i)
        return i