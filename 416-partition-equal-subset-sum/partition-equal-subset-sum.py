class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True  

        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]
        

        # total = sum(nums)
        # if total % 2 != 0:
        #     return False
        
        # target = total // 2
        # memo = {}
        
        # def dp(index,sm):

        #     if sm == target:
        #         return True

        #     if index >= len(nums) or sm > target:
        #         return False

        #     if (index,sm) in memo:
        #         return memo[(index, sm)]

        #     include = dp(index+1,sm+nums[index])
        #     not_include = dp(index+1,sm)

        #     memo[(index,sm)] = include or not_include

        #     return memo[(index, sm)]

        # return dp(0,0)



        
        