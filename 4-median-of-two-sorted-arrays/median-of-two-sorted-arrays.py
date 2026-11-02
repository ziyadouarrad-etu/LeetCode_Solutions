class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l = nums1 + nums2
        l = sorted(l)
        length = len(l)
        if length%2 == 0:
            return (l[int(length/2)] + l[int(length/2-1)])/2
        else:
            return l[int((length-1)/2)]
        