class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cs = m = sum(nums[:k])
        for i in range(k, len(nums)):
            cs += nums[i] - nums[i - k]
            m = max(m, cs)
        return m / k
