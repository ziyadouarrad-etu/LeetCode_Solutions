class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = set(arr)
        T = [i for i in range(1, arr[-1] + k + 1) if i not in s]
        print(T)
        return T[k - 1]
