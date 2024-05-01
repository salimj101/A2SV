class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        b = Counter()
        for i in words:
            word = "".join(sorted(set(i)))
            count += b[word]
            b[word] += 1
        return count
