class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l,r=0,1
        while r<len(nums):
            if nums[l]==nums[r]:
                nums.pop(r)
            else:
                l=r
                r=l+1