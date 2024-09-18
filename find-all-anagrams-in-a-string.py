class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a = []
        p_len = len(p)
        p_counts = {char: p.count(char) for char in set(p)}
        
        for i in range(len(s) - p_len + 1):  
            window = s[i:i + p_len]
            window_counts = {char: window.count(char) for char in set(window)}
            if window_counts == p_counts:
                a.append(i)
        
        return a
