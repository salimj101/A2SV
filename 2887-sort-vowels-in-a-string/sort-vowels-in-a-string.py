class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        k = []
        s= list(s)
         
        for ch in s:
            if ch in vowels:
                k.append(ch)

        k.sort()
        val = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = k[val]
                val += 1
        return ''.join(s)
                
        
