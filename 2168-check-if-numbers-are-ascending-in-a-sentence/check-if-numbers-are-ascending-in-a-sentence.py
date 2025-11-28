class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums=[int(word) for word in s.split() if word.isdigit()]
        return nums==sorted(list(set(nums)))
