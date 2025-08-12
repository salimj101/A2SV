class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrak(i,path, length):
            if len(path) == length:
                ans.append(path[:])
                return 

            for j in range(i,n):
                path.append(nums[j])
                backtrak(j+1,path,length)
                path.pop()

        ans = []
        n = len(nums)

        for _ in range(n+1):
            backtrak(0,[] , _)

        return ans