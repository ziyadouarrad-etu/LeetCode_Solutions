class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first, last = -1, -1

        # Find index of first occurence
        a, b = 0, len(nums) - 1
        while a <= b:
            c = (a + b) // 2
            if nums[c] < target:
                a = c + 1
            elif nums[c] > target:
                b = c - 1
            else:
                first = c
                b = c - 1

        # Find index of last occurence
        a, b = 0, len(nums) - 1
        while a <= b:
            c = (a + b) // 2
            if nums[c] < target:
                a = c + 1
            elif nums[c] > target:
                b = c - 1
            else:
                last = c
                a = c + 1
        return [first, last]
