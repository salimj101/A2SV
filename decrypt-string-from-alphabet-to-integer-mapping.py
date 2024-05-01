class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        p = 0
        for t in range(len(s)-1, -1, -1):
            if s[t] == "#":
                p = 2
                res.append(chr(int(s[t-2:t]) + 96))
            elif p == 0:
                res.append(chr(int(s[t])+96))
            else:
                p -= 1
        l = res[::-1]
        return "".join(l)
