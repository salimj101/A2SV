class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        or_val = 0
        for x in nums:
            or_val |= x
        return or_val * (1 << (len(nums) - 1))


        # def dfs(i, current):
        #     if i == len(nums):
        #         return current
        #     # Include nums[i]
        #     include = dfs(i + 1, current ^ nums[i])
        #     # Exclude nums[i]
        #     exclude = dfs(i + 1, current)
        #     return include + exclude
        
        # return dfs(0, 0)
