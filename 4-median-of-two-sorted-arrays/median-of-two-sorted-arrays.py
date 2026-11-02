class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        i = 0
        j = 0
        l = []

        while (i < m and j < n):
            if nums1[i] < nums2[j]:
                l.append(nums1[i])
                i += 1
            else:
                l.append(nums2[j])
                j += 1

        if (i < m):
            l.extend(nums1[i:])
            
        if (j < n):
            l.extend(nums2[j:])
        
        length = m + n
        mid = length // 2

        if length % 2 == 1:
            return l[mid]

        return (l[mid - 1] + l[mid]) / 2