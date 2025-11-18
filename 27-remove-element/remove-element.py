class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        end=len(nums)-1
        i=0
        taille=0
        while i<len(nums):
            if nums[i]!=val:
                taille+=1
                i+=1
            else:
                nums[i],nums[end]=nums[end],nums[i]
                end-=1
                if end<0:
                    break
            if i>end:
                break
        return taille