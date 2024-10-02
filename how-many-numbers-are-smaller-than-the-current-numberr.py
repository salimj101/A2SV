class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            counter=0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    counter += 1
            result.append(counter)
        return result