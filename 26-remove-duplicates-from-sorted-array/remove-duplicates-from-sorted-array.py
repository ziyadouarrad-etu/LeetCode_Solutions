class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,0
        s=set()
        while(j<len(nums)):
            if nums[j] not in s:
                s.add(nums[j])
                nums[i]=nums[j]
                i+=1
            j+=1
        return i