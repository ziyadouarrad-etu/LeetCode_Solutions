class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)

        length = m + n
        mid = length // 2

        i, j = 0, 0

        prev, curr = 0, 0

        for _ in range(mid + 1):
            prev = curr

            temp1 = nums1[i] if i < m else float("inf")   
            temp2 = nums2[j] if j < n else float("inf")

            if (temp1 < temp2):
                curr = temp1
                i += 1
            else:
                curr = temp2
                j += 1


        if length % 2:
            return curr

        return (prev + curr) / 2