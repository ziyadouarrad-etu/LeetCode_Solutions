class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        i,j=0,len(height)-1
        while i!=j:
            left=height[i]
            right=height[j]
            a=min(left, right)
            area=max(area, (j-i)*a)
            if left<right:
                i+=1
            else:
                j-=1
        return area
        