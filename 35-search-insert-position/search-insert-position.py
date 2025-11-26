class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a=0
        b=len(nums)-1
        while (a<=b):
            c=(a+b)//2
            if nums[c]==target:
                return c
            elif nums[c]>target:
                b=c-1
            else:
                a=c+1
        return a

        