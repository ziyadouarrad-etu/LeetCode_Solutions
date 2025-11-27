class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine=list(magazine)
        for c in ransomNote:
            if c in magazine:
                magazine.pop(magazine.index(c))
            else:
                return False
        return True
        