class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans= 0 
        cnt = Counter(answers)
        for key, freq in cnt.items():
            if key + 1 < freq:
                ans += (key+1) * math.ceil(freq / (key+1))
            else: 
                ans += key+1
        return ans 