class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zeros = nums.count(0)
        nums[:] = [x for x in nums if x != 0]
        nums.extend([0] * count_zeros)
