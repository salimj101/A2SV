class Solution:
    def frequencySort(self, s: str) -> str:
        s_count= Counter(s)
        l = list(sorted(s_count,key = s_count.get,reverse = True))
        return ''.join(i*s_count[i] for i in l)