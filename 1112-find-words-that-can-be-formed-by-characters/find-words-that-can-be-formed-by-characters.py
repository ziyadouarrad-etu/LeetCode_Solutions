class Solution:
    def canBeCreated(self, word: str, chars: str) -> bool:
        chars=list(chars)
        for c in word:
            if c in chars:
                chars.pop(chars.index(c))
            else:
                return False
        return True
    def countCharacters(self, words: List[str], chars: str) -> int:
        result=0
        for word in words:
            if self.canBeCreated(word, chars):
                result+=len(word)
        return result