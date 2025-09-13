class Solution:
    def maxFreqSum(self, s: str) -> int:
        ch = Counter(s)
        vowel = max((ch[i] for i in ch if i in 'aeiou'), default=0)
        consonant = max((ch[i] for i in ch if i not in 'aeiou'), default=0)
        
        return vowel + consonant