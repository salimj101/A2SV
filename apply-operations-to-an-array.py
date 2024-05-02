class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        c = nums.count(0)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] and nums[i-i] != 0:
                nums[i-1] = nums[i-1]*2
                nums[i] = 0

        zeros = nums.count(0)
        nums = [i for i in nums if i != 0]
        return nums+([0]*zeros)
