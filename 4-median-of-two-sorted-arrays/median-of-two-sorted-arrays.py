class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        length = m + n
        mid = length // 2

        i = 0
        j = 0
        c = 0

        prev = 0
        curr = 0
        while (c <= mid):
            
            temp1 = nums1[i] if i < m else float("inf")
                
            temp2 = nums2[j] if j < n else float("inf")

            prev = curr

            if (temp1 < temp2):
                curr = temp1
                i += 1
            else:
                curr = temp2
                j += 1
            c += 1


        if length % 2 == 1:
            return curr

        return (prev + curr) / 2