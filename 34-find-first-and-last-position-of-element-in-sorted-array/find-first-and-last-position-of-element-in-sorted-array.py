class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a,b=0,len(nums)-1
        while a<=b:
            c=(a+b)//2
            if nums[c]<target:
                a=c+1
            elif nums[c]>target:
                b=c-1
            else:
                while nums[a]<target:
                    a+=1
                while nums[b]>target:
                    b-=1
                return [a,b]
        return [-1, -1]
        
        


        