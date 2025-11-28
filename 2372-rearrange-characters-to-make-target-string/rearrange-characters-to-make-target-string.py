class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s = list(s)
        num_copies = 0
        while True:
            for c in target:
                if c not in s:
                    return num_copies
                s.pop(s.index(c))
            num_copies += 1
        return num_copies
