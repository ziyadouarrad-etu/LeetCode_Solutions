class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, n = 0, 1
        l = len(arr)
        while k and i < l:
            if n < arr[i]:
                k -= 1
                n += 1
            else:
                i += 1
                n += 1
        return n + k - 1
