class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        memo = {}

        def dp(row,col):
            

            if row == m-1 and col == n-1:
                return grid[row][col]

            if row >= m or col >= n:
                return float("inf")

            if (row, col) in memo:
                return memo[(row,col)]

            right = dp(row, col+1)
            down = dp(row+1, col)

            memo[(row, col)] = grid[row][col] + min(right, down)
            return memo[(row, col)]

        return dp(0,0)