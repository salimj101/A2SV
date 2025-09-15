class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        text=text.split()
        count = 0

        for i in text:
            if all(ch not in i for ch in brokenLetters):
                    count += 1
        
        return count
        