class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        t = {c: i for i, c in enumerate(s)}
        j = a = 0
        b = []
        for i, c in enumerate(s):
            j = max(j, t[c])
            if i == j:
                b.append(i - a + 1)
                a = i + 1
        return b